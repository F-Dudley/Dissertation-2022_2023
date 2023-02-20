#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import tqdm
from ProtoScan.CloudGenerators.Point_E import CloudSampler
from Images.Utils import getPathImages

srcPath = './data/duck'

# In[ ]:
# Create the Sampler
sampler = CloudSampler.CreateCloudSampler('base1B')

# In[ ]:
# Load Sample Images
images = getPathImages(srcPath)
if (len(images) == 0):
    print("No Images Found")
    exit()

# In[ ]:
# Generate Samples from the Sampler, using Obtained Images
samples = None
for x in tqdm(sampler.sample_batch_progressive(batch_size=len(images), model_kwargs=dict(images=images))):
    samples = x

# In[ ]:
# Save Samples

i = 0
for cloud in sampler.output_to_point_clouds(samples):
    with open(f'{srcPath}/cloud_{i}.npz') as f:
        cloud.save(f)

    i += 1
