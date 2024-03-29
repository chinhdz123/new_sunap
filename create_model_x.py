import torch
import torch.nn as nn
import json
import matplotlib.pyplot as plt
with open('data_json\data.json', 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)

#pre=processing for x data
x_train = json_object["x_train"]
x_test = json_object["x_test"]
label_x_train = json_object["label_x_train"]
label_x_test = json_object["label_x_test"]
label_x_max = json_object["label_x_max"]

# plt.scatter(x_train,label_x_train)
# plt.show()
X_train = []
for item in x_train:
    X_train.append([item,item**2,item**3,item**4])
X_train = torch.tensor(X_train,dtype=torch.float32)

X_test = []
for item in x_test:
    X_test.append([item,item**2,item**3,item**4])
X_test = torch.tensor(X_test,dtype=torch.float32)

label_x_train = torch.tensor(label_x_train,dtype=torch.float32)
label_x_test = torch.tensor(label_x_test,dtype=torch.float32)

label_x_train = label_x_train.view(label_x_train.shape[0], 1)
label_x_test = label_x_test.view(label_x_test.shape[0], 1)

n_samples, n_features = X_train.shape

# 1) Model
# Linear model f = wx + b
input_size = n_features
output_size = 1
model = nn.Linear(input_size, output_size)

# 2) Loss and optimizer
learning_rate = 0.001

criterion = nn.MSELoss()
# optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate,momentum=0.9)
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate,betas=[0.9,0.99])


# 3) Training loop
num_epochs = 5000
best_loss = 100
count = 0
for epoch in range(num_epochs):
    # Forward pass and loss
    label_x_predict_train = model(X_train)
    loss = criterion(label_x_predict_train, label_x_train)
    
    # Backward pass and update
    loss.backward()
    optimizer.step()

    # zero grad before new step
    optimizer.zero_grad()

    if (epoch+1) % 10 == 0:
        print(f'epoch: {epoch+1}, loss = {loss.item():.4f}')
        label_x_predict_test = model(X_test)
        loss_test = criterion(label_x_predict_test, label_x_test)
        print(f'epoch: {epoch+1}, loss_valid = {loss_test.item():.4f}')
        if loss_test < best_loss:
            best_loss = loss_test
            count = 0
        else:
            count+=1
    if count > 1000:
        break

torch.save(model, r"model\model_x.pth")

predicteds = model(X_train).detach().numpy()
print([predicted*label_x_max for predicted in predicteds])
print([label_x*label_x_max for label_x in label_x_train])
print(model.parameters())

