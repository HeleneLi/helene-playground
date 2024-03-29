import hashlib

class NeuralCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Anna sends 2 NC to Jan"
t2 = "Patrick sends 4.5 NC to Jan"
t3 = "Jan sends 3.2 NC to Patrick"
t4 = "Pia sends 0.6 NC to Anna"
t5 = "Franziska sends 0.9 NC to Daniel"
t6 = "Daniel sends 4.5 NC to Franziska"

initial_block = NeuralCoinBlock("Initial String", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = NeuralCoinBlock(initial_block.block_hash, [t3, t4])
print(second_block.block_data)
print(second_block.block_hash)

third_block = NeuralCoinBlock(second_block.block_hash, [t5, t6])
print(third_block.block_data)
print(third_block.block_hash)
