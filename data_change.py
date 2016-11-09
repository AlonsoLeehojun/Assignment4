import pydivert

with pydivert.WinDivert("(tcp.DstPort == 80 or tcp.SrcPort == 80) and tcp.PayloadLength > 0") as w:
    for packet in w:
        if packet.is_outbound:
            print("1")
            #print(packet.tcp.payload)
            #pl = packet.tcp.payload
            print("2")
            #print(pl)
            #pl.replace("Accept-Encoding: gzip", "Accept-Encoding:     ")
            #print(pl)
            packet.tcp.payload = packet.tcp.payload.replace("Accept-Encoding: gzip, ", "Accept-Encoding:       ")
            #packet.tcp.payload = pl
        if packet.is_inbound:
            print("3")
            #print(packet.tcp.payload)
            packet.tcp.payload = packet.tcp.payload.replace("Michael", "Gilbert")
        w.send(packet)
