
# What is xAPI?
xAPI is a cross-platform programming interface developed by [SS&C Eze](https://www.ezesoft.com/) allowing clients to create and manage orders as well as retrieve market data from Eze EMS. xAPI uses [gRPC](https://grpc.io/), an open source Remote Procedure Call framework initially developed by Google in 2015. gRPC technology combines HTTP/2 transport with [Protocol Buffer](https://developers.google.com/protocol-buffers/) binary serialization to offer common API functionality including support for both 1) request-response and streaming interaction patterns, 2) synchronous and asynchronous operations, and 3) convenient flow control features such as client initiated request cancellation.

## Why use a gRPC-based API?
gRPC is a good fit for Execution Management Systems as unary (request-response) interfaces are ideal for standard order operations such as create, modify, or cancel. Streaming interfaces are particularly useful for delivering market data. For example, users can subscribe to price updates for one or more securities and data is received by the client as it is available.

# How do I get started with xAPI?
The following tutorials explain how to install gRPC and compile the xAPI proto files using Protocol Buffers. Then we show you how to connect and authenticate, create and cancel an order, and retrieve order details. Python is used in this tutorial, but note that xAPI is cross-platform, supporting over 10 of the most popular [languages](https://grpc.io/docs/languages/).

You will need server details and login credentials to execute the code in the tutorials below. Contact your SS&C Eze client service representative to request details. If you do not have a sales representative, [let us know](https://info.ezesoft.com/request-a-demo) that you want try xAPI!

## Installation

If you do not have Python installed, [Anaconda](https://www.anaconda.com/) is easy to use and is good at managing multiple environments. After downloading and installing Anaconda, open an Anaconda Prompt, create an environment with the gRPC libraries and activate it with the following three commands:

    conda create --name xapi python=3.8
    conda activate xapi
    conda install grpcio grpcio-tools pandas

> **Tip**: When you open an Anaconda Prompt, you can return to the xapi environment with the `conda activate xapi` command 

Next, clone the xAPI repo to download the latest proto files:

    git clone https://github.com/ezesoft/xAPI.git

Next, use the Protocol Buffers compiler to generate native Python xAPI interfaces. xAPI includes three *proto* files:

 1. *utilities.proto*: Utility interfaces for connecting and authenticating
 2. *order.proto*: Order management interfaces for creating and cancelling orders
 3. *market_data.proto*: Interfaces for retrieving market data

In Anaconda Prompt, navigate to the tutorials folder

    cd xapi/tutorials

You can execute the following commands in the Anaconda Prompt to compile the *proto* files:

    python -m grpc_tools.protoc -I../protos --python_out=. --grpc_python_out=. ../protos/order.proto
    
    python -m grpc_tools.protoc -I../protos --python_out=. --grpc_python_out=. ../protos/utilities.proto
    
    python -m grpc_tools.protoc -I../protos --python_out=. --grpc_python_out=. ../protos/market_data.proto

The compiler generates six (6) new files: 
- Three (3) *_pb2.py* files containing the request and response classes
- Three (3) *_pb2_grpc.py* containing client and server classes.

You now are ready to write Python code to interact with the xAPI system!

# Python xAPI Tutorials

Complete code examples for all tutorials may be found [here](./tutorials/), identified by the tutorial number (e.g., *tutorial_1_connect_and_disconnect.py*, etc.). To get the most out of the following tutorials, we recommend opening the code file for the tutorial, and following along.

When you're ready, you can execute the code directly in Anaconda Prompt by invoking python and supplying the file name:

    python tutorial_1_connect_and_disconnet.py

If you don't already have one installed, there are a number of excellent Python Integrated Development Environments (IDEs) available, such as [Visual Studio Code (VSCode)](https://code.visualstudio.com/) and [PyCharm](https://www.jetbrains.com/pycharm/). 

## Tutorial 1: Connecting and Disconnecting

In this first tutorial, you will connect to xAPI, authenticate, and disconnect.

To access the xAPI Utility interfaces, import the utility modules generated above:

    import grpc
    import utilities_pb2 as util
    import utilities_pb2_grpc as util_grpc

Next, create a stub to gain access to the remote **Utility** interfaces. xAPI requires Transport Layer Security (TLS), so you must establish an encrypted connection. You can use this [roots.pem](https://pki.google.com/roots.pem) file distributed by Google, which is also included in our xAPI repository.

    with open(r'.\roots.pem', 'rb') as f: cert = f.read()
    channel = grpc.secure_channel('SERVER:PORT', grpc.ssl_channel_credentials(root_certificates=cert))
    util_stub = util_grpc.UtilityServicesStub(channel)

> **Note**: Server details and authentication credentials will be provided by your SS&C Eze representative.

Next, use the stub to connect and authenticate with xAPI.

    connect_response = util_stub.Connect(util.ConnectRequest(UserName='USER', Domain='DOMAIN', Password='PASSWORD', Locale='LOCALE'))
    print('Connect result: ', connect_response.Response)

> **Important**: If the login is successful, you will receive a UserToken in the response. Do not lose this token as it must be provided on all subsequent calls to the server.

Finally, verify the login succeeded and disconnect from the server:

    if connect_response.Response == 'success':
	   disconnect_response = util_stub.Disconnect(util.DisconnectRequest(UserToken=connect_response.UserToken))
	   print('Disconnect result: ', disconnect_response.ServerResponse)

You've now connected, authenticated, and disconnected from the server using xAPI.

> **Note**: xAPI supports Secure Remote Password ([SRP](http://srp.stanford.edu/)) protocol. See this [example](./examples/srp_connect.py) for details.


## Tutorial 2: Placing an Order
Now that you can connect and disconnect, let's look at placing an order.

To access the xAPI Order interfaces, import the order modules generated above.

    import order_pb2 as ord
    import order_pb2_grpc as ord_grpc

Next, create a stub to gain access to the remote **Order** interfaces. Since you are reusing the channel object; there is no need to recreate it.

    ord_stub = ord_grpc.SubmitOrderServiceStub(channel)

Finally, submit the order request:

    order_response = ord_stub.SubmitSingleOrder(ord.SubmitSingleOrderRequest(Symbol='TSLA', Side='BUY', Quantity=5000, Route='ROUTE', Account='ACCOUNT', OrderTag='MyOrderId', UserToken=connect_response.UserToken))
    print('Order result: ', order_response)

> **Note**: Route and Account information will be provided by your representative. 

> **Important**: When submitting an order, populate the OrderTag property with a unique identifier so you can match an order event from xAPI with an order in your system. 

Well done, you've now placed an order via xAPI.

## Tutorial 3: Getting Order Details
With an order placed, let's request order activity from xAPI to see the status and details of the order. xAPI offers both a unary, request-response and a streaming interface to retrieve order activity. Order activity includes orders you submitted to the system as well as activity on the order, such as executions (fills) or rejections. 

This tutorial provides an example of the unary *GetTodaysActivityJson* interface which returns details in a pandas-friendly JSON format.

To start, import both pandas and numpy:

    import pandas as pd
    import numpy as np

Next, optional filters are available to refine the data results. Limit the request to order submission activity by adding a single filter *IncludeUserSubmitOrder*.

    activity_response = util_stub.GetTodaysActivityJson(util.TodaysActivityJsonRequest(IncludeUserSubmitOrder=True, UserToken=connect_response.UserToken))

> **Note**: By default, all *include* filters are False.

The data is returned in JSON format and converted to a pandas DataFrame:

    df = pd.read_json(activity_response.TodaysActivityJson, convert_dates=False)

In the previous *Placing an Order* tutorial, an OrderTag was provided on the request. You can use the OrderTag to find a specific order and lookup the xAPI *OrderId*:

    xapi_order_id = df[(df['OrderTag']=='MyOrderId')]['OrderId'][0]
    print('The xAPI OrderId for my order is ', xapi_order_id)
    
> **Tip**: Use the xAPI OrderId to cancel and modify existing orders.

Now you can not only log-in and place orders, but retrieve the orders' details too!

## Tutorial 4: Getting Execution Details
Building on the Get Order Details tutorial, you can use the same interface to retrieve order execution details from xAPI by changing the filter.
 
Let's request fill activity from xAPI while adding a single filter *IncludeExchangeTradeOrder*.

    activity_response = util_stub.GetTodaysActivityJson(util.TodaysActivityJsonRequest(IncludeExchangeTradeOrder=True, UserToken=connect_response.UserToken))

The data is returned in JSON format and converted to a pandas DataFrame:

    df = pd.read_json(activity_response.TodaysActivityJson, convert_dates=False)

Finally, the following pandas aggregation will give you a summary of:
- Total filled volume
- Number of fills
- VWAP for each security with fills
<!-- end of list--> 

    if not df.empty:
	    g = df.groupby(["Symbol", "Side"]).agg( tot_filled_vol = pd.NamedAgg('Volume', 'sum'), num_fills = pd.NamedAgg('Volume', 'count'), vwap = pd.NamedAgg('Price', lambda x: np.average(x, weights=df.loc[x.index, 'Volume'])))
	    print('fills:\n', g)

> **Note**: This example uses *NamedAgg* which requires pandas [0.25](https://pandas.pydata.org/docs/whatsnew/v0.25.0.html) or later.

You now have a more complete picture of what is happening with your orders, all by only using the xAPI!

## Tutorial 5: Cancelling an Order
Up to this point, you have established a connection, placed an order, and pulled order details in xAPI. Let's look at cancelling an order.

In the *Getting Order Details* tutorial, you retrieved the xAPI *OrderId* of an order placed in the *Placing an Order* tutorial. In this tutorial, you use the OrderId to request the order be cancelled.

    cancel_response = ord_stub.CancelSingleOrder(ord.CancelSingleOrderRequest(OrderId=xapi_order_id, UserToken=connect_response.UserToken))
    print('Cancel result: ', cancel_response)

It's that simple - the order is cancelled!
## Tutorial 6: Subscribing to Market Data
Along with manipulating your own orders, you can use xAPI to retrieve market data. You can both request a market data snapshot as well as subscribe to future market data updates. This tutorial covers both the snapshot and streaming cases for Level 1 market data.

> **Tip:** While this is little different from the previous tutorials, the basics remain the same, and builds on what you've done up to this point.

​To access the xAPI Market Data interfaces, import the market_data modules generated during the **Installation**. Since gRPC streaming is a blocking operation, data coming from the server should to be processed on a separate thread so your application is not blocked. To do this, include the threading module as well.

    from threading import Thread
    import market_data_pb2 as md
    import market_data_pb2_grpc as md_grpc
​
Define a new function to process market data returned by the server:

    def  handle_data(response):
	    try:
    	for tick in response:
    		if tick.Trdprc1.DecimalValue == 0.0:
    			continue
    		print('Received market data for {0}, Last: {1}'.format(tick.DispName, tick.Trdprc1.DecimalValue))
	    except  Exception  as e:
    	print(e)

There are some important elements in this code block worth calling out. 

First, note the exception handling - this function is running on a separate thread. When the main application thread tells xAPI to cancel the stream, gRPC deliberately throws an exception to break out of the blocking call. This exception should be handled by your code. 

Second, notice the *response* variable. This is a gRPC result object which is iterable using the standard Python *for*, *list*, or *next* syntax. When you attempt to iterate this object, it will block until data is available from the server.

Moving on to the main application thread, create a stub to gain access to the remote **Market Data** interfaces:

    md_stub = md_grpc.MarketDataServiceStub(channel)

Next, request market data from the server. You can request data for one or more securities at a time:

    response = md_stub.SubscribeLevel1Ticks(md.Level1MarketDataRequest(Symbols=['TSLA'], Request=True, Advise=True, UserToken=connect_response.UserToken))

> **Note:**
>If you want a snapshot of the market data (i.e., the current values), set the *Request* parameter to *True*. 
>
>If you want to receive all subsequent market ticks (i.e., get future market data updates), set the *Advise* parameter to *True*.

Next, create and start the data handler thread and pass the iterable response object to the thread function:

    t = Thread(target=handle_data, args=(response, ))
    t.start()

At this point, your main application thread is free to do other work. When you are ready to shut down, cancel the request and join the thread to wait for it to terminate gracefully:

    response.cancel()
    t.join()

Great! You now have market data information!

## Tutorial Wrap-Up
Congratulations! You now have the foundation to start building your own custom Eze EMS integrations using Python and xAPI.

For a list of available interfaces (and associated field names) refer to the EMS xAPI Technical Reference document.

# Eze EMS xAPI Use Restrictions
As an Eze EMS xAPI user, you are prohibited from retransmitting any Eze Market Data using the Eze EMS xAPI, without the express prior written consent of Eze EMS and the exchanges or other third-party data providers (referred to as “Sources” in your end user agreement). Any unauthorized retransmission of Eze Market Data is a breach of your end user agreement and will cause immediate termination of your use of the Eze EMS, Eze Market Data, and the Eze EMS xAPI.

Any non-display usage of Eze Market Data, such as use of real- time data in algorithmic trading or program trading, is subject to the rules, regulations, and policies of the applicable exchanges and additional exchange fees may apply. In addition, you may have a non-display usage of Eze Market Data even if a display of real-time data occurs. Please review your Eze EMS end user agreement, and the exchanges’ and third-party data providers’ rules, regulations, and policies that apply to your use of the Eze EMS API (which apply to Eze EMS xAPI) and/or Eze Market Data. It is the sole responsibility of the Eze EMS xAPI user and each user receiving, directly or indirectly accessing or otherwise using Eze Market Data to determine whether your receipt, access or use is reportable and/or fee liable.
