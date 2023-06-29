from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy

#ログインしている人にだけビューをアクセスする
from django.contrib.auth.mixins import LoginRequiredMixin

from todo.models import Task

#タスクの一覧表示
class TaskListViews(ListView):
    model = Task
    template_name = 'todo/task_list.html'


#タスクの詳細を表示
class TaskDetailView(DetailView):
    model = Task
    template_name = "todo/task_detail.html"

#タスクの新規作成
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__' #全てのフォールドを使うという意味
    success_url = reverse_lazy('task-list') #どこのURLに飛ばすか

#タスクの削除
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task-list') #どこのURLに飛ばすか
    template_name = 'todo/task_delete.html'

#タスクの編集
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__' #全てのフォールドを使うという意味
    success_url = reverse_lazy('task-list') #どこのURLに飛ばすか
    #↑タスクの新規作成と同じ
