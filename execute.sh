vyper contract.vy -f bytecode > contract_bytecode.txt
vyper contract.vy -f abi > contract_abi.json
python web3_deploy.py
python -m http.server
