def process_sales(input_file="sales.txt", output_file="sales_report.txt"):
    employee_total = {}   # 직원별 총 판매금액
    total_sales = 0       # 전체 판매금액
    records = []           # 콘솔 출력용 (날짜, 이름, 상품명, 수량, 판매금액)

    # 1. 파일 읽기
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            date, name, item, qty, price = line.split(",")
            qty = int(qty)
            price = int(price)

            # 2. 판매금액 = 수량 * 단가
            amount = qty * price

            # 3. 직원별 총 판매금액 누적
            employee_total[name] = employee_total.get(name, 0) + amount

            # 4. 전체 판매금액 누적
            total_sales += amount

            records.append((date, name, item, qty, amount))

    # 5. 판매왕 찾기 (총 판매금액이 가장 큰 직원)
    top_employee = max(employee_total, key=employee_total.get)
    top_amount = employee_total[top_employee]

    # 콘솔 출력
    print(f"{'날짜':<12}{'이름':<8}{'상품명':<8}{'갯수':<6}{'판매금액'}")
    for date, name, item, qty, amount in records:
        print(f"{date:<12}{name:<8}{item:<8}{qty}개  {amount:,}원")
    print(f"전체 판매 금액 : {total_sales:,}원")
    print(f"판매왕 : {top_employee}")

    # 6. sales_report.txt 저장
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("직원별 판매 실적\n\n")
        for name, amount in employee_total.items():
            f.write(f"{name} : {amount:,}원\n")
        f.write(f"\n전체 판매 금액 : {total_sales:,}원\n")
        f.write(f"판매왕 : {top_employee} ({top_amount:,}원)\n")


process_sales()
