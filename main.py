def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """
    
    celsius = int(input())
    farenheit = (celsius * 9/5) + 32
    print(f'{farenheit:.2f}')
    
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celsius, farenheit


if __name__ == '__main__':
    main()
