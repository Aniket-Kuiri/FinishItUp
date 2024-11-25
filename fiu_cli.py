# CLI for FinishItUpAPP
import argparse
from finishitup import FinishItUp

def parse_args():
    parser = argparse.ArgumentParser(
        description='FinishItUp App Command Line Interface')
    parser.add_argument("action",
                        choices=['add_task', 'get_current_task',
                                 'complete_task', 'get_completed_tasks'],
                        help="Perform an action associated with FinishItUp App")
    parser.add_argument("--name", help="Task name")
    parser.add_argument("--type", choices=['one-time', 'repetitive'],
                        help="Task type either one-time or repetitive")
    parser.add_argument("--description", help="Task description")
    parser.add_argument("--task_id", help="Task unique id")
    parser.add_argument("--terminate", action='store_true', dest='terminate', 
                        help="Terminate a repetitive task")
    args = parser.parse_args()
    if args.action == 'add_task' and not args.name:
        parser.error("--name is required when the action is 'add_task'")
    if args.action == 'add_task' and not args.type:
        parser.error("--type is required when the action is 'add_task'")
    if args.action == 'add_task' and not args.description:
        parser.error("--description is required when the action is 'add_task'")
    if args.action == 'complete_task' and not args.task_id:
        parser.error("--task_id is required when the action is 'complete_task'")
    if args.action == 'complete_task' and not args.description:
        parser.error("--description is required when the action is 'complete_task'")
    return args

def main():
    args = parse_args()
    action = args.action
    finishitup = FinishItUp()

    if action == 'add_task':
        is_success = finishitup.add_task(args.name, args.type, args.description)
        if  not is_success:
            print("Failed to add task")
        else:
            print("Task added successfully")

    elif action == 'get_current_task':
        task = finishitup.get_current_task()
        if  task == None:
            print("No task open at present")
        else:
            print(task)

    elif action == 'complete_task':
        is_success, error = finishitup.complete_task(args.task_id, args.description, args.terminate)
        if  not is_success:
            print(f"Failed to complete task, reason: {error}")

    elif action == 'get_completed_tasks':
        task_list = finishitup.get_completed_tasks()
        if  task_list == None:
            print("No completed tasks")
        else:
            for task in task_list:
                print(task) 

    elif action == 'reset':
        is_success = finishitup.reset()
        if not is_success:
            print("Failed to reset")
        else:
            print("Reset complete")

if __name__ == "__main__":
    main()