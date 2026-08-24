.text
.globl main
main:
    sub $8, %rsp
    lea msg(%rip), %rdi  # 【核心修改】利用 RIP 相对寻址计算 msg 地址，完美支持 PIE
    call printf
    add $8, %rsp
    ret
msg:
    .asciz "Hello\n"

