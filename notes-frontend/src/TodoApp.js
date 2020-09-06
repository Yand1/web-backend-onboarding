import React from 'react';
import { TodoFooter } from './components/TodoFooter';
import { TodoHeader } from './components/TodoHeader';
import { TodoList } from './components/TodoList';
import './style.css';

let index = 0;

export default class TodoApp extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      todos: {},
      filter: 'all'
    };
  }

  render() {
    const { filter, todos } = this.state;
    return (
      <div>
        <TodoHeader addTodo={this._addTodo} setFilter={this._setFilter} filter={filter} />
        <TodoList complete={this._complete} todos={todos} filter={filter} />
        <TodoFooter clear={this._clear} todos={todos} />
      </div>
    );
  }

  _addTodo = label => {
    const { todos } = this.state;
    const id = index++;

    this.setState({
      todos: { ...todos, [id]: { label, completed: false } }
    });
  };

  _complete = id => {
    const { todos } = this.state;
    const todo = todos[id];
    const newTodos = { ...todos, [id]: { ...todo, completed: !todo.completed } };

    this.setState({
      todos: newTodos
    });
  };

  _clear = () => {
    const { todos } = this.state;
    const newTodos = {};

    Object.keys(this.state.todos).forEach(id => {
      if (!todos[id].completed) {
        newTodos[id] = todos[id];
      }
    });

    this.setState({
      todos: newTodos
    });
  };

  _setFilter = filter => {
    this.setState({
      filter: filter
    });
  };
}