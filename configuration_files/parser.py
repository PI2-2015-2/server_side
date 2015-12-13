import json
from collections import OrderedDict
import execInstructionsProcedural as instruction


class Parser():
    def parseJson(self, jsonFile):
        try:
            # Loads the Json file in a OrderedDict
            parsed_json = json.load(open('instruction.json'), object_pairs_hook=OrderedDict)

            size = len(parsed_json)
            j = 0
            # Remove any numeric from the key of the command
            while j < size:
                string = parsed_json.keys()[j]
                result = ''.join([i for i in string if not i.isdigit()])
                parsed_json.keys()[j] = result

            i = 0
            while i < size:
                # Execute inside loop instructions
                if(parsed_json.keys()[i] == 'loop'):
                    for k in range(0, parsed_json.values()[i].get('loops')):
                        for j in range(i+1, i+1+parsed_json.values()[i].get('instructions')):
                            instruction.run(parsed_json.keys()[j], parsed_json.values()[j])
                    # Jump to the next instruction outside the loop
                    i += 1+parsed_json.values()[i].get('instructions')
                else:
                    # execute instruction
                    instruction.run(parsed_json.keys()[i], parsed_json.values()[i])
                    i += 1
            # Clean PWM
            instruction.cleanPWM()
        except KeyboardInterrupt:
            print "keyboard interrupt"
        except:
            print "exception"
        finally:
            instruction.cleanGPIO()
