import torch
import torch.nn as nn

# Simple model
model = nn.Linear(2, 1)

# Dummy data
x = torch.randn(10, 2)
y = torch.randn(10, 1)

criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Training
for epoch in range(5):
    optimizer.zero_grad()
    output = model(x)
    loss = criterion(output, y)
    loss.backward()
    optimizer.step()

# Save model
torch.save(model.state_dict(), "model.pth")

# Save output
with open("output.txt", "w") as f:
    f.write(f"Training complete. Final loss: {loss.item()}")