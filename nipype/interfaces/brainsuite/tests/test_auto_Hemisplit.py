# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..brainsuite import Hemisplit


def test_Hemisplit_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputHemisphereLabelFile=dict(argstr='-l %s',
    mandatory=True,
    ),
    inputSurfaceFile=dict(argstr='-i %s',
    mandatory=True,
    ),
    outputLeftHemisphere=dict(argstr='--left %s',
    genfile=True,
    ),
    outputLeftPialHemisphere=dict(argstr='-pl %s',
    genfile=True,
    ),
    outputRightHemisphere=dict(argstr='--right %s',
    genfile=True,
    ),
    outputRightPialHemisphere=dict(argstr='-pr %s',
    genfile=True,
    ),
    pialSurfaceFile=dict(argstr='-p %s',
    ),
    terminal_output=dict(nohash=True,
    ),
    timer=dict(argstr='--timer',
    ),
    verbosity=dict(argstr='-v %d',
    ),
    )
    inputs = Hemisplit.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Hemisplit_outputs():
    output_map = dict(outputLeftHemisphere=dict(),
    outputLeftPialHemisphere=dict(),
    outputRightHemisphere=dict(),
    outputRightPialHemisphere=dict(),
    )
    outputs = Hemisplit.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
