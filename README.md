Отримані результати вказують на те, що обидва алгоритми правильно обробляють вхідні дані та видають очікуваний результат. Однак, щоб об'єктивно порівняти їх ефективність, потрібно провести більш докладне дослідження, включаючи аналіз часу виконання та обчислювальної складності для різних вхідних даних.

### Аналіз ефективності алгоритмів:

- **Жадібний алгоритм**: Має лінійну складність O(n), де n - кількість монет, і працює швидше, але не завжди гарантує оптимальний результат.
- **Алгоритм динамічного програмування**: Має квадратичну складність O(n * m), де n - сума для видачі, а m - кількість різних номіналів монет, і забезпечує оптимальний результат.

### Результати:

1. **При обробці суми 113**:
   - **Жадібний алгоритм**: Результат: {50: 2, 10: 1, 2: 1, 1: 1}, Час виконання: приблизно 1.91 мікросекунд.
   - **Алгоритм динамічного програмування**: Результат: {1: 1, 2: 1, 10: 1, 50: 2}, Час виконання: близько 34.09 мікросекунд.

2. **При обробці суми 50000**:
   - **Жадібний алгоритм**: Результат: {50: 1000}, Час виконання: приблизно 2.15 мікросекунд.
   - **Алгоритм динамічного програмування**: Результат: {50: 1000}, Час виконання: близько 15.67 мілісекунд.

### Висновки:

- Обидва алгоритми забезпечують очікуваний результат для обох вхідних сум.
- У випадку суми 113, жадібний алгоритм працює значно швидше за алгоритм динамічного програмування.
- При обробці суми 50000 також жадібний алгоритм виявився набагато ефективнішим.
- Жадібний алгоритм може бути кращим вибором, коли швидкість виконання є важливішою, особливо для великих сум.
- Алгоритм динамічного програмування може бути кращим вибором, коли оптимальність результату має велике значення, а час виконання менш критичний.
