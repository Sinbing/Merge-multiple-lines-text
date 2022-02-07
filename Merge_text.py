while True:
    input_counter, temp_input, doc_output = 1, 'null', ''
    while True:
        while temp_input != '':
            temp_input = str(input(f'- {input_counter}:\n'))
            if input_counter == 1:
                output_string = temp_input
            else:
                output_string = output_string + temp_input
            input_counter = input_counter + 1
        doc_flag = input('- stop input? -\n')
        if doc_flag != '':
            doc_output = doc_output + output_string + '\n' + doc_flag
            temp_input, output_string = 'null', ''
        else:
            doc_output = doc_output + output_string
            break   
    fill = int((int((int(len(doc_output)) - 10)) / 2)) * '='
    print(f' {fill} OUTPUT {fill} \n{doc_output}\n {fill}========{fill} ')
    return_flag = input(' -- input "y" to exit --\n')
    if return_flag == 'y':
        break