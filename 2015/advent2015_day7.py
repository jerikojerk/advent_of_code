

INI_FILE="2015\\advent2015_day7-input.txt"
from pprint import pprint
import re


class WireAction:
    def __init__(self,capture:dict,univers:dict):
        self.assign=capture['assign']
        self.value=None
        self.circuit=univers

        if capture['int1']:
            self.int1=int(capture['int1'])
        elif capture['var1']:
            self.var1=capture['var1']    
        if len(capture) >3:
            if capture['int2']:
                self.int2=int(capture['int2'])
            elif capture['var2']:
                self.var2=capture['var2']
        self.circuit[self.assign]=self
        
    def _calculate(self, n):
        attr = f"int{n}"
        if hasattr(self, attr):
            return getattr(self, attr)
        attr = f"var{n}"
        if hasattr(self, attr):
            varname = getattr(self, attr)
            if varname in self.circuit:
                return self.circuit[varname].calculate()
            else:
                raise ValueError(f"{varname} is not defined")
        raise RuntimeError("Missing attribute")


    def calculate(self):
        print ( "DOWN:"+self.toString())
        if self.value is None:
            self.value=self._execute()
        print ( "UP:"+self.toString())
        return self.value

    def _execute(self):
       raise RuntimeError("shall not execute it")

    def toString(self)->str:
        op=self.__class__.__name__[3:]
        left = self.int1 if hasattr(self,'int1') else self.var1 if hasattr(self,'var1') else ""
        right = self.int2 if hasattr(self,'int2') else self.var2 if hasattr(self,'var2') else ""
        info = self.value if self.value is not None else "?"
        return f"{left} {op} {right} -> {self.assign} #{info}"

    def reset(self):
        self.value = None
    
    def override(self,over):
        self.value = over 


class BitSet(WireAction): 
    def _execute(self):
        return self._calculate(1)


class BitNot(WireAction):
    def _execute(self):
        op1=self._calculate(1)
        return ~op1 & 0xFFFF

class BitAnd(WireAction):   
    def _execute(self):
        op1=self._calculate(1)
        op2=self._calculate(2)
        return (op1 & op2 ) & 0xFFFF

class BitOr(WireAction):
    def _execute(self):
        op1=self._calculate(1)
        op2=self._calculate(2)
        return (op1 | op2 ) & 0xFFFF

class BitRshift(WireAction):
    def _execute(self):
        op1=self._calculate(1)
        offset=self._calculate(2)
        return  (op1 >> offset) & 0xFFFF

class BitLshift(WireAction):
    def _execute(self):
        op1=self._calculate(1)
        offset=self._calculate(2)
        return  (op1 << offset) & 0xFFFF


#pattern 
pattern_op1= r"(?:(?P<var1>[a-z]+)|(?P<int1>\d+))"
pattern_op2= r"(?:(?P<var2>[a-z]+)|(?P<int2>\d+))"
pattern_res= r"(?P<assign>[a-z]+)"
patterns={
    "SET":      (re.compile(rf"{pattern_op1}\s*->\s*{pattern_res}"),BitSet),
    "NOT":      (re.compile(rf"NOT\s+{pattern_op1}\s*->\s*{pattern_res}"),BitNot),
    "AND":      (re.compile(rf"{pattern_op1}\s+AND\s+{pattern_op2}\s*->\s*{pattern_res}"),BitAnd),
    "OR":       (re.compile(rf"{pattern_op1}\s+OR\s+{pattern_op2}\s*->\s*{pattern_res}"),BitOr),
    "LSHIFT":   (re.compile(rf"{pattern_op1}\s+LSHIFT\s+{pattern_op2}\s*->\s*{pattern_res}"),BitLshift),
    "RSHIFT":   (re.compile(rf"{pattern_op1}\s+RSHIFT\s+{pattern_op2}\s*->\s*{pattern_res}"),BitRshift)
}


def parser ( line:str, patterns:dict,univers:dict):
    clean=line.strip()
    if "AND" in clean:
        (pattern,func) = patterns["AND"]
    elif "OR" in clean:
        (pattern,func) = patterns["OR"]
    elif "LSHIFT" in clean:
        (pattern,func) = patterns["LSHIFT"]
    elif "RSHIFT" in clean:
        (pattern,func) = patterns["RSHIFT"]
    elif "NOT" in clean:
        (pattern,func) = patterns["NOT"]
    else:
        (pattern,func) = patterns["SET"]

    m = pattern.fullmatch( clean )
    if m:
        #print( "matcched whith ",repr(m) )
        #pprint( m.groupdict())
        func(m.groupdict(),univers)
            
    else:
       raise ValueError( f"syntaxe non comprise {clean}")

circuit={}



with open(INI_FILE, "r") as instructions:
    for instruction in instructions:
        instruction=instruction.strip()
        parser( instruction , patterns, circuit )

result = circuit['a'].calculate()

print(f"hello Santa, resultat= {result}")

for wire in circuit.values():
    wire.reset()

circuit['b'].override(result)

result2= circuit['a'].calculate()

print(f"hello Santa, new resultat= {result2}")






