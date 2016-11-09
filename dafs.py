import pydivert

print("start")

with pydivert.WinDivert("tcp and tcp.PayloadLength > 0") as w:
    for packet in w:
        if(packet.is_outbound):
            data = packet.tcp.payload
            data = data.replace(b'Accept-Encoding: gzip', b'Accept-Encoding:     ')
            packet.tcp.payload = data
        if(packet.is_inbound):
            data = packet.tcp.payload
            data = data.replace(b'Michael', b'Gilbert')
            packet.tcp.payload = data
        w.send(packet, recalculate_checksum=True)

print("done")