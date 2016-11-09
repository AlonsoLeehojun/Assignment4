import pydivert

with pydivert.WinDivert("(tcp.DstPort == 80 or tcp.SrcPort == 80) and tcp.PayloadLength > 0") as w:
    for packet in w:
        if packet.is_outbound:
            print("1")
            #print(packet.tcp.payload)
            print("2")
            packet.tcp.payload = packet.tcp.payload.replace("Accept-Encoding: gzip, ", "Accept-Encoding:       ")

        if packet.is_inbound:
            print("3")
            #print(packet.tcp.payload)
            packet.tcp.payload = packet.tcp.payload.replace("Michael", "Gilbert")
        w.send(packet)
