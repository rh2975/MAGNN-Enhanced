import torch

print("GPUs available:", torch.cuda.device_count())
for i in range(torch.cuda.device_count()):
    print(f"GPU {i}: {torch.cuda.get_device_name(i)}")



# import torch
# print(torch.version.cuda)
# print(torch.backends.cudnn.version())

