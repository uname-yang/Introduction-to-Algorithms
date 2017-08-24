def get_crc32_text(text):
    _poly = 0xEDB88320
    _crc  = 0xFFFFFFFF
    for item in text:
        comp = (_crc ^ ord(item)) & 0xFF
        for i in range(0,8):
            comp = (_poly ^ (comp >>1)) if (comp & 1) else (comp >> 1)
        _crc = ( ( _crc >> 8 ) & 0x00FFFFFF ) ^ comp
    return _crc ^ 0xFFFFFFFF