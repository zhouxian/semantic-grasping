import dexnet
import os
import dexnet.database.database as db
from autolab_core import YamlConfig
from dexnet.visualization import DexNetVisualizer3D as vis

DEXNET_DIR = os.path.realpath(os.path.dirname(os.path.realpath(dexnet.__file__)) + '/../../') + '/'
DEXNET_API_DEFAULTS_FILE = DEXNET_DIR + 'cfg/api_defaults.yaml'
default_config = YamlConfig(DEXNET_API_DEFAULTS_FILE)
for key in ['gripper_dir', 'cache_dir']:
    if not os.path.isabs(default_config[key]):
        default_config[key] = os.path.realpath(DEXNET_DIR + default_config[key])
config = default_config.config
cache_dir = config['cache_dir']
database_path = '/home/zhouxian/semantic_grasping/dexnet_2_database.hdf5'
database = db.Hdf5Database(database_path, access_level=db.READ_WRITE_ACCESS, cache_dir=cache_dir)

dataset_name = database.datasets[0].name
dataset = database.dataset(dataset_name)

object_names = dataset.object_keys
obj = dataset[object_names[0]]

vis.figure(bgcolor=(1,1,1), size=(1000,1000))
vis.mesh(obj.mesh.trimesh, color=(0.5, 0.5, 0.5), style='surface')
vis.show(animate=config['animate'])
