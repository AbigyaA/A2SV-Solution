class Solution:
    def interpret(self, command: str) -> str:
        mapping = {"()": "o", "(al)": "al"}
        interpretation = ""
        i=0
        while i < len(command):
            if command[i] == "G":
                interpretation += command[i]
                i+=1
            else:
                if command[i+1] == ")":
                    interpretation += mapping["()"]
                    i+=2
                else:
                    interpretation += mapping["(al)"]
                    i+=4
        return interpretation
