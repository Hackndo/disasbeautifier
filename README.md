# DisasBeautifier

Description
===========

Take `disas` ouput from gdb (either intel or at&t syntax), parse it and write it in output_file

Usage
=====

```sh
$ git clone git@github.com:Hackndo/disasbeautifier.git
$ cd disasbeautifier
$ chmod +x disasbeautifier.py
$ ./disasbeautifier.py input_file output_file
```

Example
=======

Input file input.disas

```
   0x0804844c <+0>:  push   ebp
   0x0804844d <+1>:  mov    ebp,esp
   0x0804844f <+3>:  sub    esp,0x28
   0x08048452 <+6>:  mov    eax,DWORD PTR [ebp+0x8]
   0x08048455 <+9>:  mov    DWORD PTR [esp+0x4],eax
   0x08048459 <+13>: lea    eax,[ebp-0x10]
   0x0804845c <+16>: mov    DWORD PTR [esp],eax
   0x0804845f <+19>: call   0x8048320 <strcpy@plt>
   0x08048464 <+24>: lea    eax,[ebp-0x10]
   0x08048467 <+27>: mov    DWORD PTR [esp],eax
   0x0804846a <+30>: call   0x8048330 <puts@plt>
   0x0804846f <+35>: leave  
   0x08048470 <+36>: ret
   0x08048471 <+0>:  push   ebp
   0x08048472 <+1>:  mov    ebp,esp
   0x08048474 <+3>:  and    esp,0xfffffff0
   0x08048477 <+6>:  sub    esp,0x10
   0x0804847a <+9>:  cmp    DWORD PTR [ebp+0x8],0x2
   0x0804847e <+13>: je     0x804848e <main+29>
   0x08048480 <+15>: mov    DWORD PTR [esp],0x8048540
   0x08048487 <+22>: call   0x8048330 <puts@plt>
   0x0804848c <+27>: jmp    0x804849e <main+45>
   0x0804848e <+29>: mov    eax,DWORD PTR [ebp+0xc]
   0x08048491 <+32>: add    eax,0x4
   0x08048494 <+35>: mov    eax,DWORD PTR [eax]
   0x08048496 <+37>: mov    DWORD PTR [esp],eax
   0x08048499 <+40>: call   0x804844c <func>
   0x0804849e <+45>: mov    eax,0x0
   0x080484a3 <+50>: leave  
   0x080484a4 <+51>: ret
```

```sh
$ ./disasbeautifier.py input.disas output.disas
```

output.disas

```asm
   0x0804844c <+0>:  push   ebp                        ; 
   0x0804844d <+1>:  mov    ebp,esp                    ; 
   0x0804844f <+3>:  sub    esp,0x28                   ; 
   0x08048452 <+6>:  mov    eax,DWORD PTR [ebp+0x8]    ; 
   0x08048455 <+9>:  mov    DWORD PTR [esp+0x4],eax    ; 
   0x08048459 <+13>: lea    eax,[ebp-0x10]             ; 
   0x0804845c <+16>: mov    DWORD PTR [esp],eax        ; 
   0x0804845f <+19>: call   0x8048320 <strcpy@plt>     ; strcpy()
   0x08048464 <+24>: lea    eax,[ebp-0x10]             ; 
   0x08048467 <+27>: mov    DWORD PTR [esp],eax        ; 
   0x0804846a <+30>: call   0x8048330 <puts@plt>       ; puts()
   0x0804846f <+35>: leave                             ; 
   0x08048470 <+36>: ret                               ; 

 ***************************************************** ; 

   0x08048471 <+0>:  push   ebp                        ; 
   0x08048472 <+1>:  mov    ebp,esp                    ; 
   0x08048474 <+3>:  and    esp,0xfffffff0             ; 
   0x08048477 <+6>:  sub    esp,0x10                   ; 
   0x0804847a <+9>:  cmp    DWORD PTR [ebp+0x8],0x2    ; 
   0x0804847e <+13>: je     0x804848e <main+29>        ; 

   0x08048480 <+15>: mov    DWORD PTR [esp],0x8048540  ; 
   0x08048487 <+22>: call   0x8048330 <puts@plt>       ; puts()
   0x0804848c <+27>: jmp    0x804849e <main+45>        ; 
   0x0804848e <+29>: mov    eax,DWORD PTR [ebp+0xc]    ; 
   0x08048491 <+32>: add    eax,0x4                    ; 
   0x08048494 <+35>: mov    eax,DWORD PTR [eax]        ; 
   0x08048496 <+37>: mov    DWORD PTR [esp],eax        ; 
   0x08048499 <+40>: call   0x804844c <func>           ; func()
   0x0804849e <+45>: mov    eax,0x0                    ; 
   0x080484a3 <+50>: leave                             ; 
   0x080484a4 <+51>: ret                               ; 

 ***************************************************** ; 
```

Contribute
==========

* Parse call arguments
* Detect functions
* Detect loops
* Draw arrows for jumps
