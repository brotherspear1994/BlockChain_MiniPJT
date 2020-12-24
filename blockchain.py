from hashlib import sha256
from datetime import datetime

# haslib를 활용해 sha256을 구현하는법 이해하기 연습
# test_content = 'test string for making hash'
# test_hash = sha256(test_content.encode())
# print(test_hash.hexdigest())

# 블록체인을 만들어보자
class Block:
    def __init__(self, prevhash, nonce=0):
        # 후에 POW 과정을 거치며 nonce 값을 자동으로 조정해줄거임.
        self.timestamp = datetime.now() # 아쉬우니간 생성시간도 만들어줌
        # self.data = name  # 초기에는 테스틀 위해 블록의 이름은 클래수 변수에 내가 직접 입력해주는 것으로 설정함.
        self.data = input() # 블록을 생성 할 때 그냥 이름을 직접 입력해주자.(자동으로 이름을 만들어주기 귀찮다,,ㅎㅎ)
        self.prevhash = prevhash
        self.nonce = nonce
        # generate_hash() 함수를 직접 만들어서 해시를 생성
        self.hash = self.generate_hash()

    def print_block(self): # 구현 결과를 확인하기 위한 프린트문
        print("nonce: ", self.nonce)
        print("data: ", self.data)
        print("prevhash: ", self.prevhash)
        print("hash: ", self.generate_hash())

    def generate_hash(self):
        # block contents의 nonce 변수를 변경해 해시값도 함께 변경해주도록 구현
        block_contents = str(self.nonce)+str(self.prevhash)
        block_hash = sha256(block_contents.encode())
        return block_hash.hexdigest()

# 블록이 잘 만들어지는지 확인
# Genesis_Block = Block("Genesis Block", 1, 0, 0)
# test = Block(0)
# Genesis_Block.print_block()
# test.print_block()


# 이전에 만든 블록을 가지고 실제로 이전 블록과 다음 블록을 연결하는 BlockChain 만들기
class Blockchain:
    def __init__(self):
        self.chain = [] # 모든 블록을 저장할 chain list
        self.genesis_block()
    # genesis block(첫 블록)을 생성하는 메소드 추가
    def genesis_block(self):
        block = Block(0)
        self.chain.append(block)
        return self.chain
    # 새로운 block 추가하기
    def add_block(self):
        previous_block_hash = self.chain[len(self.chain)-1].hash # block 리스트(chain)에서 가장 마지막 놈의 hash 값을 가져옴
        new_block = Block(previous_block_hash) # 이전 해시값을 가진 새로운 블록 생성
        proof = self.proof_of_work(new_block) # 00000으로 시작하는 hash 값과 이를 위한 nonce 값을 지니도록 만들어줌.
        self.chain.append(new_block) # 완료됐다면 chain에 추가.
        return proof, new_block

    # 블록체인 작업증명 함수 추가(POW)
    # difficulty = 5 로 설정함으로써 자동으로 내부에서 00000으로 시작하는 hash 값을 찾기위해 계속 nonce값을 더해간다.
    def proof_of_work(self, block, difficulty=5):
        proof = block.generate_hash()

        while proof[:5] != '0'*difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        return proof

# test = Blockchain()
# genesis block이 잘 만들어졌는지 확인
# print(test.chain)

# 새로운 블록 추가
# test.add_block()
# 새로운 블락이 추가된것을 확인 할 수 있다.
# print(test.chain)

# 전체 배열의 마지막 블록도 출력해보자
# print(test.chain[-1])

HyunchangChain = Blockchain()
# print(HyunchangChain.chain) # Genesis block 잘 만들어졌는지 확인

# 명세서대로 3개 이상의 블록을 추가로 만들어 주자.
# 나 같은 경우는 세개의 블럭을 추가로 만들어 chain에 총 4개의 블록이 담기게 했다.
# 각각의 이름
'''
Genesis Block
2nd
3rd
4th
'''
for _ in range(3):
    HyunchangChain.add_block()
# 잘 만들어졌는지 확인
# print(HyunchangChain.chain)

# 결과물 출력
for block in HyunchangChain.chain:
    block.print_block()
    print()

# 꽤 빠르게 출력됨을 알 수 있다. 만약 difficulty 를 올리면 출력 시간이 기하급수적으로 늘어나게 된다.
# 성공적으로 이번 과제를 수행했음을 알 수 있다.