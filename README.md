disasbeautifier
==============

gdb disas output beautifier

Description
===========

Take disas ouput from gdb (either intel or at&t syntax), parse it and write it in output_file

Usage
=====

```python
./disasbeautifier input_file output_file
```

Ouput example
=============

```asm
   0x80484dd:  push   ebp                              ; 
   0x80484de:  mov    ebp,esp                          ; 
   0x80484e0:  sub    esp,0x28                         ; 
   0x80484e3:  mov    eax,ds:0x8049a08                 ; 
   0x80484e8:  test   eax,eax                          ; 
   0x80484ea:  jne    0x8048504                        ; 

   0x80484ec:  mov    eax,0x8049940                    ; 
   0x80484f1:  mov    ds:0x8049a08,eax                 ; 
   0x80484f6:  mov    DWORD PTR [esp],0x80486a0        ; 
   0x80484fd:  call   0x8048380 <printf@plt>           ; printf()
   0x8048502:  jmp    0x804853f                        ; 
   0x8048504:  mov    eax,ds:0x8049a0c                 ; 
   0x8048509:  add    eax,0x8049940                    ; 
   0x804850e:  movzx  eax,BYTE PTR [eax]               ; 
   0x8048511:  xor    eax,0x53                         ; 
   0x8048514:  mov    BYTE PTR [ebp-0x9],al            ; 
   0x8048517:  mov    eax,ds:0x8049a0c                 ; 
   0x804851c:  movzx  edx,BYTE PTR [ebp-0x9]           ; 
   0x8048520:  mov    BYTE PTR [eax+0x8049940],dl      ; 
   0x8048526:  mov    eax,ds:0x8049a0c                 ; 
   0x804852b:  add    eax,0x1                          ; 
   0x804852e:  mov    ds:0x8049a0c,eax                 ; 
   0x8048533:  cmp    BYTE PTR [ebp-0x9],0xcc          ; 
   0x8048537:  je     0x804853f                        ; 

   0x8048539:  cmp    BYTE PTR [ebp-0x9],0xc3          ; 
   0x804853d:  jne    0x8048504                        ; 

   0x804853f:  leave                                   ; 
   0x8048540:  ret                                     ; 

 ***************************************************** ; 

   0x8048541:  push   ebp                              ; 
   0x8048542:  mov    ebp,esp                          ; 
   0x8048544:  and    esp,0xfffffff0                   ; 
   0x8048547:  sub    esp,0x30                         ; 
   0x804854a:  mov    DWORD PTR [esp+0x2c],0x8049940   ; 
   0x8048552:  mov    eax,DWORD PTR [esp+0x2c]         ; 
   0x8048556:  and    eax,0xfffff000                   ; 
   0x804855b:  mov    DWORD PTR [esp+0x28],eax         ; 
   0x804855f:  mov    eax,DWORD PTR [esp+0x28]         ; 
   0x8048563:  mov    edx,DWORD PTR [esp+0x2c]         ; 
   0x8048567:  sub    edx,eax                          ; 
   0x8048569:  mov    eax,edx                          ; 
   0x804856b:  mov    DWORD PTR [esp+0x24],eax         ; 
   0x804855f:  mov    eax,DWORD PTR [esp+0x28]         ; 
   0x8048563:  mov    edx,DWORD PTR [esp+0x2c]         ; 
   0x8048567:  sub    edx,eax                          ; 
   0x8048569:  mov    eax,edx                          ; 
   0x804856b:  mov    DWORD PTR [esp+0x24],eax         ; 
   0x804856f:  mov    DWORD PTR [esp+0x18],0x0         ; 
   0x8048577:  mov    DWORD PTR [esp+0x1c],0x0         ; 
   0x804857f:  mov    DWORD PTR [esp+0x4],0x80484dd    ; 
   0x8048587:  mov    DWORD PTR [esp],0x5              ; 
   0x804858e:  call   0x8048390 <signal@plt>           ; signal()
   0x8048593:  mov    eax,DWORD PTR [esp+0x24]         ; 
   0x8048597:  lea    edx,[eax+0xc1]                   ; 
   0x804859d:  mov    eax,DWORD PTR [esp+0x28]         ; 
   0x80485a1:  mov    DWORD PTR [esp+0x8],0x7          ; 
   0x80485a9:  mov    DWORD PTR [esp+0x4],edx          ; 
   0x80485ad:  mov    DWORD PTR [esp],eax              ; 
   0x80485b0:  call   0x8048370 <mprotect@plt>         ; mprotect()
   0x80485b5:  int3                                    ; 

   0x80485b6:  lea    eax,[esp+0x18]                   ; 
   0x80485ba:  mov    DWORD PTR [esp+0x4],eax          ; 
   0x80485be:  mov    DWORD PTR [esp],0x80486b3        ; 
   0x80485c5:  call   0x80483d0 <__isoc99_scanf@plt>   ; __isoc99_scanf()
   0x80485ca:  int3                                    ; 

   0x80485cb:  mov    ecx,DWORD PTR ds:0x8049a08       ; 
   0x80485d1:  mov    eax,DWORD PTR [esp+0x18]         ; 
   0x80485d5:  mov    edx,DWORD PTR [esp+0x1c]         ; 
   0x80485d9:  mov    DWORD PTR [esp],eax              ; 
   0x80485dc:  mov    DWORD PTR [esp+0x4],edx          ; 
   0x80485e0:  call   ecx                              ; 
   0x80485e2:  test   eax,eax                          ; 
   0x80485e4:  je     0x80485f4                        ; 

   0x80485e6:  mov    DWORD PTR [esp],0x80486b8        ; 
   0x80485ed:  call   0x80483a0 <puts@plt>             ; puts()
   0x80485f2:  jmp    0x8048600                        ; 
   0x80485f4:  mov    DWORD PTR [esp],0x80486c2        ; 
   0x80485fb:  call   0x80483a0 <puts@plt>             ; puts()
   0x8048600:  mov    eax,0x0                          ; 
   0x8048605:  leave                                   ; 
   0x8048606:  ret                                     ; 

 ***************************************************** ; 
```
