# FAQ

## How can I track an order?

When you create an order using xAPI, you may specify an external identifier in the OrderTag property. xAPI will include the OrderTag in all update messages. This mechanism allows you to match orders between your system and ours.

When you request order activity using either the **Unary** GetActivityJson or the **Streaming** SubscribeOrderInfo API, the OrderTag property will contain the value you specified.

If you do not supply a value to OrderTag at the time an order is created, you will have to match orders between your system and ours based on properties such as symbol and quantity.

## What is the difference between Unary and Streaming APIs?

GetActivityJson is an example of a **Unary** RPC. The client makes a request and gets a single response. **Unary** is sometimes referred to as the _request-response_ communication pattern.

SubscribeOrderInfo is an example of a **Streaming** RPC. The client makes a request and receives data from the server as it is available. Technically, when calling a **Streaming** API, the client is provided an iterator object; each time the client accesses the iterator (typically in a loop), the client is blocked until data is available from the server.

Since **streaming** RPC blocks an application, you should loop through the iterator object from a dedicated thread.

A good example of a **Streaming** RPC is market data: the client requests live price updates for a security and receives the updates as they arrive from the exchange.

## Do we need to use heartbeat for having session up for longer time

No. XAPI does auto renew though there is inactivity from client for up until hours like mentioned above. Heartbeat is needed if we are planning to use streaming (subscription) APIs.

## We see heart beat response like UNKNOWN/DEAD. How should we handle this?	
	1. LIVE- No action needed. All good.
	2. UNKNOWN / DEAD- From client-side, re-establish GRPC connection and call connect API again.
	
## Why do we need heartbeat on client side?	
	1. This is needed if clients call streaming APIs. The reason here is to detect if there is a disconnection from client's end while sending the heart beat response and if so, we would dispose (logout) that user from xAPI end and the given token wouldn't work forward.
	2. With sticky session in place, it wouldn't be needed for clients only calling request-response APIs.