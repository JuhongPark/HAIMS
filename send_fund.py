from web3 import Web3

# Ganache 로컬 블록체인에 연결
ganache_url = "http://127.0.0.1:7545"  # Ganache의 RPC URL
web3 = Web3(Web3.HTTPProvider(ganache_url))

# 연결 확인
if not web3.is_connected():
    print("Ganache와의 연결에 실패했습니다.")
    exit()

# 보낼 계정과 받을 계정 설정
sender_account = "0x7BA02dE606Fad283111bB5da1A862d788Be57a1A"  # 보내는 계정 (첫 번째 계정)
recipient_account = "0x756de5Af92e660baA067aC253dd68872063EB6cd"  # 받는 계정

# 전송할 이더리움 양 (1 ETH)
amount = web3.to_wei(1, 'ether')  # 1 ETH

# 트랜잭션 생성
tx = {
    'from': sender_account,
    'to': recipient_account,
    'value': amount,
    'gas': 2000000,
    'gasPrice': web3.to_wei('20', 'gwei'),
    'nonce': web3.eth.get_transaction_count(sender_account),
}

# 트랜잭션 서명 및 전송
signed_tx = web3.eth.account.sign_transaction(tx, private_key='0xf785f74417699e2945f8422e09c24efa3c26a197baecef50e84d2bd4e2dfbef6')  # YOUR_PRIVATE_KEY를 입력하세요.
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

# 트랜잭션 해시 출력
print(f"Transaction hash: {web3.to_hex(tx_hash)}")

