def main():
    def fibonacci(n):
        val = 0
        i = 0
        if n < 1:
            return(0)
        else:
            for m in range(n):
                no = val + i
                i = val
                val = no
                return(no)

    print(fibonacci(0))
if __name__ == "main": main()
