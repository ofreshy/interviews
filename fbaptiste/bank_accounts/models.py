from abc import ABC
from dataclasses import dataclass
import datetime
from enum import Enum
import uuid


def generate_id():
    """

    """
    return str(uuid.uuid4())[0:8]


@dataclass
class Person:
    id_: str
    first_name: str
    last_name: str
    middle_name: str

    def __post_init__(self):
        self.first_name = self.first_name.lower().capitalize()
        self.last_name = self.last_name.lower().capitalize()
        self.middle_name = self.middle_name.lower().capitalize()

    def full_name(self):
        if self.middle_name:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.last_name}"


class PeopleFactory:
    def __init__(self):
        self._people = dict()

    def new(self, first_name: str, last_name: str, middle_name: str = ""):
        person = Person(
            id_=generate_id(),
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
        )
        self._people[person.id_] = person
        return person


class TransactionCommand(ABC):
    pass


@dataclass
class Deposit(TransactionCommand):
    value: float

    def __post_init__(self):
        if self.value <= 0:
            raise ValueError(
                f"Deposit value must be positive and was {self.value}"
            )


@dataclass
class Interest(TransactionCommand):
    value: float

    def __post_init__(self):
        if self.value < 0 or self.value > 1:
            raise ValueError(
                f"Interest value must be between 0-1 inc. and was {self.value}"
            )


@dataclass
class Withdraw(TransactionCommand):
    value: float

    def __post_init__(self):
        if self.value < 0 or self.value > 10000:
            raise ValueError(
                f"Withdraw value must be between 0-10000 inc. and was {self.value}"
            )


@dataclass
class BankAccount:
    id_: str
    person: Person
    time_zone: datetime.tzinfo
    _balance: float = 0
    _overdraft: float = 0

    def deposit(self, deposit: Deposit):
        self._balance += deposit.value

    def interest(self, interest: Interest):
        if not self.is_overdrawn():
            self._balance *= (1 + interest.value)

    def withdraw(self, withdraw: Withdraw):
        new_balance = self._balance - withdraw.value
        if new_balance < self._overdraft * -1:
            raise ValueError(" cannot exceed overdraft")
        self._balance = new_balance

    @property
    def balance(self):
        return self._balance

    @property
    def overdraft(self):
        return self._overdraft

    @overdraft.setter
    def overdraft(self, value):
        self._overdraft = value

    def is_overdrawn(self):
        return self._balance < 0


class BankAccountFactory:

    def __init__(self):
        self._accounts = dict()

    def open(
            self,
            person: Person,
            time_zone: datetime.tzinfo = datetime.timezone.utc,
            overdraft: float = 0,
    ):
        if overdraft > 10000:
            raise ValueError("overdraft cannot exceed 10000")
        account = BankAccount(
            id_=generate_id(),
            person=person,
            time_zone=time_zone,
            _overdraft=overdraft,
        )
        self._accounts[account.id_] = account
        return account


class TransactionStatus(Enum):
    APPROVED = 1
    REJECTED = 2


@dataclass
class TransactionDetails:
    bank_account_id: str
    person_details: str
    transaction_date: str
    balance_before: float

    @classmethod
    def from_bank_account(cls, bank_account: BankAccount):
        return cls(
            bank_account_id=bank_account.id_,
            person_details=bank_account.person.full_name(),
            transaction_date=datetime.datetime.now(tz=bank_account.time_zone).isoformat(),
            balance_before=bank_account.balance
        )


@dataclass
class TransactionResult:
    status: TransactionStatus
    balance_after: float

    @classmethod
    def from_bank_account(
            cls,
            account: BankAccount,
            status: TransactionStatus,
    ):
        return cls(
            balance_after=account.balance,
            status=status,
        )


@dataclass
class Transaction:
    id_: str
    command: TransactionCommand
    details: TransactionDetails
    result: TransactionResult


class TransactionFactory:
    def __init__(self):
        self._transactions = dict()

    def _apply(self, bank_account: BankAccount, command, command_func):
        details = TransactionDetails.from_bank_account(bank_account)
        try:
            command_func(command)
            status = TransactionStatus.APPROVED
        except ValueError:
            status = TransactionStatus.REJECTED

        result = TransactionResult.from_bank_account(bank_account, status=status)

        transaction = Transaction(
            id_=generate_id(),
            details=details,
            command=command,
            result=result,
        )
        self._transactions[transaction.id_] = transaction
        return transaction

    def deposit(self, bank_account: BankAccount, value: float):
        return self._apply(
            bank_account=bank_account,
            command=Deposit(
                value=value,
            ),
            command_func=bank_account.deposit,
        )

    def withdraw(self, bank_account: BankAccount, value: float):
        return self._apply(
            bank_account=bank_account,
            command=Withdraw(
                value=value,
            ),
            command_func=bank_account.withdraw,
        )

    def apply_interest(self, bank_account: BankAccount, value: float):
        return self._apply(
            bank_account=bank_account,
            command=Interest(
                value=value,
            ),
            command_func=bank_account.interest,
        )


class IST(datetime.tzinfo):
    def tzname(self, dt):
        "datetime -> string name of time zone."
        return "ist"

    def utcoffset(self, dt):
        "datetime -> timedelta, positive for east of UTC, negative for west of UTC"
        return datetime.timedelta(minutes=180)

    def dst(self, dt):
        """datetime -> DST offset as timedelta, positive for east of UTC.

        Return 0 if DST not in effect.  utcoffset() must include the DST
        offset.
        """
        return datetime.timedelta(minutes=120)


# singleton
ist = IST()
