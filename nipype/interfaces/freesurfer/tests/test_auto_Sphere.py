# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..utils import Sphere


def test_Sphere_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    copyfile=True,
    mandatory=True,
    position=-2,
    ),
    in_smoothwm=dict(copyfile=True,
    ),
    magic=dict(argstr='-q',
    ),
    num_threads=dict(),
    out_file=dict(argstr='%s',
    hash_files=False,
    name_source=['in_file'],
    name_template='%s.sphere',
    position=-1,
    ),
    seed=dict(argstr='-seed %d',
    ),
    subjects_dir=dict(),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = Sphere.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_Sphere_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Sphere.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
