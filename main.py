
import subprocess
import math
import matplotlib.pyplot as plt
import japanize_matplotlib

file_name = "main.py"
command = "git log --stat | grep {}".format(file_name)
proc = subprocess.Popen(
    command,
    shell  = True,
    stdin  = subprocess.PIPE,
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)

stdout, stderr = proc.communicate()
decode_stdout = stdout.decode('utf-8', 'ignoore').strip()
split_decode_stdout = decode_stdout.split('\n')
split_decode_stdout.reverse()
parsed = []
for v in split_decode_stdout:
    vv = list(filter(None, v.split('|')[1].split(' ')))
    parsed.append([int(vv[0]), vv[1].count('+'), vv[1].count('-')])

x = []
y = []
i = 1
total_y = 0
for v in parsed:
    x.append(i)
    z = int(v[0]*(v[1]/(v[1] + v[2])))
    if z == 0:
        total_y += -v[0]
        y.append(total_y)
    else:
        total_y += z
        y.append(total_y)
    i += 1

fig = plt.figure()

ax = fig.add_subplot()
ax.plot(x, y)

plt.title('{} のコミット数と､行増減の合計の関係'.format(file_name))
plt.xlabel('{} の更新コミット数 [commit]'.format(file_name))
plt.ylabel('{} の行増減の合計 [行]'.format(file_name))

plt.show()