from web3 import Web3
from eth_account import Account

# Включение функционала неаудированных HD-кошельков
Account.enable_unaudited_hdwallet_features()

file_path = "sidka.txt"
output_file_path = "приватки.txt"

# Открываем файл для чтения
with open(file_path, "r") as file:
    # Открываем файл для записи
    with open(output_file_path, "w") as output_file:
        # Читаем seed-фразы построчно
        for line in file:
            # Удаляем лишние пробелы и символы новой строки
            seed_phrase = line.strip()

            # Создание кошелька из seed-фразы
            account = Account.from_mnemonic(seed_phrase)

            # Получение приватного ключа
            private_key = account._private_key.hex()

            # Создание объекта Web3
            w3 = Web3()

            # Получение адреса из приватного ключа
            address = w3.to_checksum_address(account.address)

            # Записываем результаты в файл
            output_file.write(f"{private_key}\n")

print("Результаты записаны в файл: ", output_file_path)
