from math import log10

__base32 = '0123456789bcdefghjkmnpqrstuvwxyz'
__decodemap = { }

for i in range(len(__base32)):
    __decodemap[__base32[i]] = i
del i

def decode_exactly(geohash):
    lat_interval, lon_interval = (-90.0, 90.0), (-180.0, 180.0)
    lat_err, lon_err = 90.0, 180.0
    is_even = True
    for c in geohash:
        cd = __decodemap[c]
        for mask in [16, 8, 4, 2, 1]:
            if is_even: # adds longitude info
                lon_err /= 2
                if cd & mask:
                    lon_interval = ((lon_interval[0]+lon_interval[1])/2, lon_interval[1])
                else:
                    lon_interval = (lon_interval[0], (lon_interval[0]+lon_interval[1])/2)
            else:      # adds latitude info
                lat_err /= 2
                if cd & mask:
                    lat_interval = ((lat_interval[0]+lat_interval[1])/2, lat_interval[1])
                else:
                    lat_interval = (lat_interval[0], (lat_interval[0]+lat_interval[1])/2)
            is_even = not is_even
    lat = (lat_interval[0] + lat_interval[1]) / 2
    lon = (lon_interval[0] + lon_interval[1]) / 2
    return lat, lon, lat_err, lon_err

def decode(geohash):
    lat, lon, lat_err, lon_err = decode_exactly(geohash)
    # Format to the number of decimals that are known
    lats = "%.*f" % (max(1, int(round(-log10(lat_err)))) - 1, lat)
    lons = "%.*f" % (max(1, int(round(-log10(lon_err)))) - 1, lon)
    if '.' in lats: lats = lats.rstrip('0')
    if '.' in lons: lons = lons.rstrip('0')
    return lats, lons

def encode(latitude, longitude, precision=12):
    lat_interval, lon_interval = (-90.0, 90.0), (-180.0, 180.0)
    geohash = []
    bits = [ 16, 8, 4, 2, 1 ]
    bit = 0
    ch = 0
    even = True
    while len(geohash) < precision:
        if even:
            mid = (lon_interval[0] + lon_interval[1]) / 2
            if longitude > mid:
                ch |= bits[bit]
                lon_interval = (mid, lon_interval[1])
            else:
                lon_interval = (lon_interval[0], mid)
        else:
            mid = (lat_interval[0] + lat_interval[1]) / 2
            if latitude > mid:
                ch |= bits[bit]
                lat_interval = (mid, lat_interval[1])
            else:
                lat_interval = (lat_interval[0], mid)
        even = not even
        if bit < 4:
            bit += 1
        else:
            geohash += __base32[ch]
            bit = 0
            ch = 0
    return ''.join(geohash)

def neighbor(geohash,direction):
    (lat, lon, lat_err, lon_err)=decode_exactly(geohash)
    neighborLat=lat+direction[0]*lat_err*2
    neighborLon=lon+direction[1]*lon_err*2
    return encode(neighborLat, neighborLon, len(geohash))

def __encodeNeighbor(lat,lon,lat_err, lon_err,direction,length):
        neighbor_lat = lat + direction[0] * lat_err;
        neighbor_lon = lon + direction[1] * lon_err;
        return encode(neighbor_lat, neighbor_lon,length )

def neighbors(geohash):
    hashstringLength=len(geohash)
    (lat, lon, lat_err, lon_err)=decode_exactly(geohash)

    neighborHashList=[
                    __encodeNeighbor(lat, lon, lat_err*2, lon_err*2,[-1,1],hashstringLength),
                    __encodeNeighbor(lat, lon, lat_err*2, lon_err*2,[0,1],hashstringLength),
                    __encodeNeighbor(lat, lon, lat_err*2, lon_err*2,[1,1],hashstringLength),
                    __encodeNeighbor(lat, lon, lat_err*2, lon_err*2,[-1,0],hashstringLength),
                    __encodeNeighbor(lat, lon, lat_err*2, lon_err*2,[0,0],hashstringLength),
                    __encodeNeighbor(lat, lon, lat_err*2, lon_err*2,[1,0],hashstringLength),
                    __encodeNeighbor(lat, lon, lat_err*2, lon_err*2,[-1,-1],hashstringLength),
                    __encodeNeighbor(lat, lon, lat_err*2, lon_err*2,[0,-1],hashstringLength),
                    __encodeNeighbor(lat, lon, lat_err*2, lon_err*2,[1,-1],hashstringLength)
    ]
    return neighborHashList
