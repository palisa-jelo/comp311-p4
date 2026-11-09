    # addi 
    addi x4, x0, -20        
    addi x5, x4, 0x7F0      
    addi x6, x5, 0x701      
    addi x7, x6, 0x531      

    # andi  
    andi x14, x6, 0x123     
    andi x15, x14, 0x71C    
    andi x17, x15, 0x541    

    # slti (
    slti x18, x4, 311       # set x18 = (x4 < 311) ? 1 : 0
    slti x19, x18, 2        # set x19 = (x18 < 2) ? 1 : 0
    slti x20, x19, 0        # set x20 = (x19 < 0) ? 1 : 0
    slti x21, x20, -3       # set x21 = (x20 < -3) ? 1 : 0
    slti x22, x21, 5        # set x22 = (x21 < 5) ? 1 : 0
    addi x0,  x22, 0        # write to x0 is ignored (still 0)
    slti x23, x4,  -20      
    addi x0,  x23, 0
    slti x24, x11, -90     
    addi x0,  x24, 0
    slti x25, x4,  0        
    addi x0,  x25, 0
    slti x26, x11, 600      
    addi x0,  x26, 0
    slti x27, x4,  -1       
    addi x0,  x27, 0

    # add 

    # sub

    # or

    # and

    # slt

    # sll 

    # srl

    # sra
