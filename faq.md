# FAQ

## How can I track an order?

When you create an order using xAPI, you may specify an external identifier in the OrderTag property. xAPI will include the OrderTag in all update messages. This mechanism allows you to match orders between your system and ours.

When you request order activity using either the **Unary** GetActivityJson or the **Streaming** SubscribeOrderInfo API, the OrderTag property will contain the value you specified.

In case you did not specify a value to OrderTag during the order creation, then you will have to match the orders between your system and ours based on properties such as symbol and quantity.

## What is the difference between Unary and Streaming APIs?

GetActivityJson is an example of a **Unary** RPC. You make a request and get a single response. Unary is sometimes referred to as the request-response communication pattern.

SubscribeOrderInfo is an example of a **Streaming** RPC. You make a request and receive data from the server as it is available. Technically, when calling a Streaming API, you are provided an iterator object; each time you accesses the iterator (typically in a loop), you are blocked until data is available from the server.

Since **streaming** RPC blocks an application, you should loop through the iterator object from a dedicated thread.

A good example of a **Streaming** RPC is market data: you request live price updates for a security and receive the updates as they arrive from the exchange.

## Can Eze OMS/Eze EMS user trigger automated compliance rule from EMS xAPI

Yes, as an Eze EMS xAPI user you can trigger the automated compliance rule from EMS xAPI and run automated compliance checks for EMS xAPI originated order. This setting is configured in Eze OMS and is similar to the process in Eze EMS.

The FID used for this is **COMPLIANCE_USER_OPTION_FLAGS (31640) w/ Flag = NO_TOUCH_AUTO_COMPLIANCE (1). Additionally the extended fields that are to be included with the order are EZE_OMS_MANAGER;EZE_OMS_TRADER;CUSTODIAN**

## How to login using SRP?	
EMS xAPI supports both SRP and non-SRP login methods. To login using SRP method your domain has to be SRP enabled. If your domain is SRP enabled, both the SRP and standard login methods work. If your domain is not SRP enabled, then only the standard login will work
	
## How can I know if my EMS xAPI session is active?	
You can subscribe to SubscribeHeartBeat API, to know your EMS xAPI connection status. On subscribing to this API, you will be intimated and requested to reconnect if an active connection with the server is terminated.

## Why was my account temporarily locked after multiple login attempts?
Your account will be temporarily locked for 3 minutes if you attempt to log in three (3) times within a 60-second period, irrespective of whether those attempts are successful or not. This security measure is in place to prevent unauthorized access and protect your account from potential misuse.


# Frequently Asked Questions for existing Eze EMS users

## What is EMS xAPI?
EMS xAPI is our next‑generation, language‑agnostic API framework for accessing EMS functions. It is designed to replace the legacy Excel API over time. EMS xAPI supports all legacy Excel API capabilities, along new enhancements and performance improvements.

## What technology is used in EMS xAPI?
EMS xAPI is built using two modern frameworks: **gRPC** and **REST**. It supports multiple programming languages, including **C#**, **Java**, **Go**, and **Python**.

## Where can I find more information on EMS xAPI?
You can refer to the EMS xAPI resources on our dedicated <a href="https://github.com/ezesoft/xapi/tree/master" target="_blank">GitHub</a> page.

 - Product <a href="https://github.com/ezesoft/xapi/tree/master/documentation" target="_blank">documentation</a>

 - <a href="https://github.com/ezesoft/xapi/tree/master/samplescripts" target="_blank">Sample code</a> for common workflows

 - <a href="https://github.com/ezesoft/xapi/tree/master/protos" target="_blank">Proto files</a>

## Why should you consider migrating to EMS xAPI?
Key reasons to migrate include:
 - It represents the future direction of EMS API development.

 - It will eventually replace the legacy Excel API.

 - The Excel API is now in maintenance‑only mode with no future roadmap.

 - All new product enhancements and roadmap initiatives are developed and delivered exclusively on EMS xAPI.

 - Support for the legacy Excel API is limited to production‑critical (severity 1) issues

## What are the prerequisites for moving from the Excel/legacy API to EMS xAPI?
To migrate, you will need:
 - An understanding of gRPC or REST frameworks.

 - A list of your current Excel API workflows that need migration.

 - Testing cycles for the migrated workflows and code.

 - A separate EMS xAPI login, required when using both the EMS terminal and xAPI concurrently.

## Good-to-know information when migrating from the Excel API to EMS xAPI.
 - The migration primarily focuses on technology modernization, since your existing workflow logic from the Excel API can be reused.

 - EMS xAPI is an evolution of the Excel API.

 - Our engagement team will support you throughout the migration process.

 - You may choose one of two migration approaches:

   - Migrate all workflows at once.

   - Phased:

     - Phase 1: Migrate existing workflows like for like.

     - Phase 2: Add new EMS xAPI workflows and enhancements of interest.