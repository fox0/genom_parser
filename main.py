RNK = {
    'AUG': '(Ile/I) Изолейцин - старт-кодон',
    'AUU': '(Ile/I) Изолейцин - альтернативный старт-кодон',
    'AUA': '(Ile/I) Изолейцин - альтернативный старт-кодон',
    'AUC': '(Ile/I) Изолейцин',
    'AAA': '(Lys/K) Лизин',
    'AAG': '(Lys/K) Лизин',
    'GGU': '(Gly/G) Глицин',
    'GGG': '(Gly/G) Глицин',
    'GGA': '(Gly/G) Глицин',
    'GGC': '(Gly/G) Глицин',
    'UAC': '(Tyr/Y) Тирозин',
    'UAU': '(Tyr/Y) Тирозин',
    'CUU': '(Leu/L) Лейцин',
    'CUA': '(Leu/L) Лейцин',
    'CUC': '(Leu/L) Лейцин',
    'CUG': '(Leu/L) Лейцин - альтернативный старт-кодон',
    'UUA': '(Leu/L) Лейцин',
    'UUG': '(Leu/L) Лейцин',
    'CCC': '(Pro/P) Пролин',
    'CCA': '(Pro/P) Пролин',
    'CCU': '(Pro/P) Пролин',
    'CCG': '(Pro/P) Пролин',
    'AGG': '(Arg/R) Аргинин',
    'AGA': '(Arg/R) Аргинин',
    'UAA': 'Стоп-кодон (Охра) даже сквозная трансляция не может проходить',
    'UAG': 'Стоп-кодон (Янтарь)',
    'UGA': 'Стоп-кодон (Опал)',
    'CAA': '(Gln/Q) Глутамин',
    'CAG': '(Gln/Q) Глутамин',
    'ACC': '(Thr/T) Треонин',
    'ACA': '(Thr/T) Треонин',
    'ACG': '(Thr/T) Треонин - альтернативный старт-кодон',
    'ACU': '(Thr/T) Треонин',
    'AAC': '(Asn/N) Аспарагин',
    'AAU': '(Asn/N) Аспарагин',
    'UCG': '(Ser/S) Серин',
    'UCA': '(Ser/S) Серин',
    'UCU': '(Ser/S) Серин',
    'UCC': '(Ser/S) Серин',
    'UGU': '(Cys/C) Цистеин',
    'UGC': '(Cys/C) Цистеин',
    'GUU': '(Val/V) Валин',
    'GUA': '(Val/V) Валин',
    'GUG': '(Val/V) Валин',
    'GUC': '(Val/V) Валин',
    'UUU': '(Phe/F) Фенилаланин',
    'UUC': '(Phe/F) Фенилаланин',
    'GCU': '(Ala/A) Аланин',
    'GCC': '(Ala/A) Аланин',
    'GCA': '(Ala/A) Аланин',
    'GCG': '(Ala/A) Аланин',
    'CGG': '(Arg/R) Аргинин',
    'CGA': '(Arg/R) Аргинин',
    'CGU': '(Arg/R) Аргинин',
    'CGC': '(Arg/R) Аргинин',
    'CAU': '(His/H) Гистидин',
    'CAC': '(His/H) Гистидин',
    'GAC': '(Asp/D) Аспарагиновая кислота',
    'GAU': '(Asp/D) Аспарагиновая кислота',
    'AGU': '(Ser/S) Серин',
    'AGC': '(Ser/S) Серин',
    'GAA': '(Glu/E) Глутаминовая кислота',
    'GAG': '(Glu/E) Глутаминовая кислота',
    'UGG': '(Trp/W) Триптофан',
}


def dnk2rnk(kodon: str):
    return kodon.replace('T', 'U')


def main():
    # https://www.ncbi.nlm.nih.gov/nuccore/MN908947.3?report=fasta
    with open('dnk.txt') as f:
        text = f.read().replace('\n', '')

    # кто-то должен перевести днк в рнк
    # (две цепочки, одна из них "зеркальная" и некодирующая + читается с двух концов)
    for i in range(0, len(text), 3):
        kodon = text[i:i + 3]
        r = dnk2rnk(kodon)
        print('{:3} {} {} - {}'.format(i, kodon, r, RNK[r]))


if __name__ == '__main__':
    main()
