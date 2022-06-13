
from sys import stdin, argv

new_adapt = argv[1]
new_adapt_len = len(new_adapt)

for line in stdin:
    read_name, error, *rest = line.rstrip('\n').split('\t')
    if int(error) < 0:
        read_seq, read_qual, *other = rest
        print('@%s\n%s\n+\n%s' % (read_name, read_seq, read_qual))
    else:
        start, end, seq_left, seq_adapt, seq_right, adapter_name, qual_left, qual_adapt, qual_right, *other = rest
        adapt_len = adapt_len_top = len(seq_adapt)
        if adapt_len_top > new_adapt_len:
            adapt_len_top = new_adapt_len
        start_offset = len(seq_left)
        end_offset = len(seq_right)
        if start_offset == 0:
            seq_adapt = new_adapt[-adapt_len_top:]
            qual_adapt = qual_adapt[-adapt_len_top:]
        elif end_offset == 0:
            seq_adapt = new_adapt[:adapt_len_top]
            qual_adapt = qual_adapt[:adapt_len_top]
        else:
            seq_adapt = new_adapt
            qual_adapt = qual_adapt[0:new_adapt_len] + qual_adapt[-1] * (new_adapt_len - adapt_len)
        print('@%s\n%s%s%s\n+\n%s%s%s' % (read_name, seq_left, seq_adapt, seq_right, qual_left, qual_adapt, qual_right))
