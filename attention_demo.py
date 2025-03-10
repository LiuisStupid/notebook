import torch
import torch.nn as nn
import torch.optim as optim

class PositionAwareReverseModel(nn.Module):
    def __init__(self, d_model, seq_len):
        super().__init__()
        self.seq_len = seq_len
        self.d_model = d_model
        
        # 位置编码层
        self.pos_embed = nn.Parameter(torch.randn(1, seq_len, d_model))
        
        # 注意力机制
        self.attention = nn.MultiheadAttention(d_model, num_heads=2, batch_first=True)
        
        # 增强的投影网络
        self.proj = nn.Sequential(
            nn.LayerNorm(d_model),
            nn.Linear(d_model, d_model*2),
            nn.ReLU(),
            nn.Linear(d_model*2, d_model)
        )

    def forward(self, x):
        # 添加位置编码
        x = x + self.pos_embed
        
        # 自注意力计算
        attn_out, _ = self.attention(x, x, x)
        
        # 残差连接
        x = x + attn_out
        
        # 最终投影
        return self.proj(x)

# 改进的训练配置
seq_len = 6
d_model = 6
batch_size = 128
epochs = 50000

# 初始化模型
model = PositionAwareReverseModel(d_model, seq_len)
optimizer = optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-5)
criterion = nn.L1Loss()  # 使用更适合离散输出的损失函数

# 改进的训练数据生成
def generate_batch(batch_size):
    # 生成包含结构化和随机数据的混合样本
    # base = torch.eye(seq_len).unsqueeze(0).repeat(batch_size//2, 1, 1)
    noise = torch.randn(batch_size - batch_size//2, seq_len, seq_len)
    # return torch.cat([base, noise], dim=0)
    return noise

# 训练循环
for epoch in range(epochs):
    x = generate_batch(batch_size)
    target = x.flip(1)  # 行倒序
    
    output = model(x)

    loss = criterion(output, target)
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if (epoch+1) % 100 == 0:
        print(f"Epoch {epoch+1}/{epochs} | Loss: {loss.item():.4f}")

# 增强的测试验证
test_input = torch.eye(seq_len).unsqueeze(0)
with torch.no_grad():
    test_output = model(test_input)

print("\n改进后的测试结果：")
print("输入矩阵：\n", test_input.squeeze().numpy())
print("\n预测输出：\n", test_output.squeeze().numpy())
print("\n预测输出（取整）：\n", test_output.squeeze().numpy().round())
print("\n期望输出：\n", test_input.squeeze().flip(0).numpy())
