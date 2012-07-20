=================
kombu-multibroker
=================

A terrible hack that allows the "kombu" package to talk to multiple brokers, and (kinda) ignore ones that are down. It also sort of provides load balancing.

When specifying the broker, use the "multiamqp" transport and specify the list of brokers as the hostname, delimited by commas.

It only supports librabbitmq.

Again, this is a terrible hack and probably *NOT* fit for general consumption at this point.

Usage
=====

    import kombu
    import kombu_multibroker

    BrokerConnection("multiamqp://broker1,broker2,broker3/")


