.text
.globl _start
_start:
    mov $1, %rax       # write syscall number (Linux x86_64 = 1)
    mov $1, %rdi       # stdout fd = 1
    lea msg(%rip), %rsi
    mov $6, %rdx       # len
    syscall
    mov $60, %rax      # exit syscall (Linux = 60)
    xor %rdi, %rdi
    syscall
msg:
    .ascii "Hello\n"
