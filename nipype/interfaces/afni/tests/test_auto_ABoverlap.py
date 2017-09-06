# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import ABoverlap


def test_ABoverlap_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file_a=dict(argstr='%s',
    copyfile=False,
    mandatory=True,
    position=-3,
    ),
    in_file_b=dict(argstr='%s',
    copyfile=False,
    mandatory=True,
    position=-2,
    ),
    no_automask=dict(argstr='-no_automask',
    ),
    out_file=dict(argstr=' |& tee %s',
    position=-1,
    ),
    outputtype=dict(),
    quiet=dict(argstr='-quiet',
    ),
    terminal_output=dict(nohash=True,
    ),
    verb=dict(argstr='-verb',
    ),
    )
    inputs = ABoverlap.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ABoverlap_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = ABoverlap.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
