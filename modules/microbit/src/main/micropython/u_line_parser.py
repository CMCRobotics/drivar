
# Very simple and probably buggy line protocol parser
# Do not reuse !

def _pop_head_or_none(arr, peek_only = False):
    if arr and len(arr)>0:
        if peek_only:
          return arr[0]
        else:
          return arr.pop(0)
    else:
        return None


def parse_lineprotocol_message(msg):
    measurement = None
    tags = {}
    values = {}
    value = None

    fragments = msg.split(" ")
    fragment = _pop_head_or_none(fragments)
    if fragment is not None:
        measurementFragments = fragment.split(",")
        if len(measurementFragments) > 0:
            measurement = measurementFragments[0]
        if  len(measurementFragments) > 1:
            for tagFragment in measurementFragments[1:]:
                tagKV = tagFragment.split("=")
                tags[tagKV[0]] = tagKV[1]
        
    fragment = _pop_head_or_none(fragments,True)
    if fragment is not None:
        if("=" in fragment):
            fragment = _pop_head_or_none(fragments)
            valuesFragment = fragment.split(",")
            for valueFragment in map(lambda v: v.split("="),valuesFragment):
                values[valueFragment[0]] = valueFragment[1]

    fragment = _pop_head_or_none(fragments)
    if fragment is not None:
        value = float(fragment)
        
    return (measurement, tags, values, value)
