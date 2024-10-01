# Vyper 스마트 계약: 자산 운용사 기능

# 투자자 구조체 정의
struct Investor:
    investment_balance: uint256
    invested: bool

# 투자자들의 정보를 저장할 스토리지 변수
investors: public(HashMap[address, Investor])

# 자산 운용사 주소 설정 (정확한 대소문자 사용)
asset_manager_address: constant(address) = 0x1234567890AbcdEF1234567890aBcdef12345678  # 자산 운용사 주소

# 최대 투자자 수
MAX_INVESTORS: constant(uint256) = 10

# 모든 투자자 주소를 저장하기 위한 배열
investor_addresses: public(address[MAX_INVESTORS])  # 최대 10명의 투자자
investor_count: public(uint256)  # 현재 투자자 수

# 입금 이벤트 정의
event Deposit:
    investor: indexed(address)
    amount: uint256

# 입금 기록을 저장하기 위한 맵 (여기서는 사용하지 않음)
# deposit_records: public(map(address, uint256))  # 각 투자자의 입금 기록

# 자산 입금 함수
@external
@payable
def deposit():
    investor: address = msg.sender
    amount: uint256 = msg.value

    # 투자자 정보를 기록
    if not self.investors[investor].invested:
        self.investors[investor] = Investor({investment_balance: amount, invested: True})
        if self.investor_count < MAX_INVESTORS:  # 최대 10명만 기록
            self.investor_addresses[self.investor_count] = investor
            self.investor_count += 1

    else:
        self.investors[investor].investment_balance += amount

    # 입금 이벤트 로그
    log Deposit(investor, amount)

    # 입금 기록 업데이트를 위해 맵을 사용하지 않고, 현재 투자자의 잔액으로 처리
    # self.deposit_records[investor] += amount  # 총 입금액 업데이트 (사용하지 않음)

# 특정 투자자의 잔액 조회 함수
@view
@external
def get_balance(investor: address) -> uint256:
    return self.investors[investor].investment_balance

# 입금 기록 조회 함수
@view
@external
def get_deposit_record(investor: address) -> uint256:
    # 현재의 입금 기록은 투자자의 투자 잔액으로 대체
    return self.investors[investor].investment_balance  # 특정 투자자의 입금 기록 반환

