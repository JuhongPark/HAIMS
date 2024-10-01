from web3 import Web3
import json

# Ganache 로컬 블록체인에 연결
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# 연결 확인
if not web3.is_connected():  # isConnected()를 is_connected()로 수정
    print("Ganache와의 연결에 실패했습니다.")
    exit()

# 첫 번째 계정을 사용하여 스마트 계약 배포
account = web3.eth.accounts[0]

# ABI 및 바이트코드 불러오기
with open('contract_abi.json') as f:
    contract_abi = json.load(f)

with open('contract_bytecode.txt') as f:
    contract_bytecode = f.read().strip()  # 공백 및 줄바꿈 제거

# 스마트 계약 객체 생성
Contract = web3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)

# 스마트 계약 배포
tx_hash = Contract.constructor().transact({'from': account})
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

# 배포된 스마트 계약 주소 출력
contract_address = tx_receipt.contractAddress
print(f"스마트 계약이 배포되었습니다: {contract_address}")

# ABI와 계약 주소를 JSON 파일에 저장
with open('contract_info.json', 'w') as f:
    json.dump({
        'address': contract_address,
        'abi': contract_abi  # 리스트 형식을 그대로 사용
    }, f)
print("contract_info.json 파일이 생성되었습니다.")
