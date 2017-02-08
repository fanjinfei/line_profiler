try:
    import types
    import line_profiler
    from grapheekdb.backends.data import keys
    keys.build_key = profile(keys.build_key)
    from grapheekdb.backends.data.operations import Addition
    for fname, f in Addition.__dict__.items():
        if isinstance(f, types.FunctionType):
            setattr(Addition, fname, profile(f))
    from grapheekdb.backends.data.base import BaseGraph, Edge, Node
    BaseGraph._add_edge = profile(BaseGraph._add_edge)
    BaseGraph._bulk_add_edge = profile(BaseGraph._bulk_add_edge)
    Edge._add_denorm_data = profile(Edge._add_denorm_data)
    Node._add_denorm_src_data = profile(Node._add_denorm_src_data)
    Node._add_denorm_tgt_data = profile(Node._add_denorm_tgt_data)
except ImportError:
    pass
