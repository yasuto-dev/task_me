from django.views.generic import ListView
from .models import DirectMessage
from django.contrib.auth import get_user_model
from django.views.generic import FormView, ListView
from django.shortcuts import redirect
from .forms import DirectMessageForm

user = get_user_model()

# #----DM一覧ページ------


# class InboxView(ListView):
#     template_name = 'inbox.html'
#     model = DirectMessage
#     context_object_name = 'messages'

#     def get_queryset(self):
#         return DirectMessage.objects.filter(recipient=self.request.user)

#---view--
class InboxView(ListView):
    template_name = 'inbox.html'
    context_object_name = 'chat_partners'

    def get_queryset(self):
        # ログインユーザーが送信したメッセージを取得し、送信相手を特定する
        sent_messages = DirectMessage.objects.filter(sender=self.request.user)
        chat_partners = {}
        for message in sent_messages:
            chat_partners[message.recipient] = message.timestamp

        # テンプレートに渡すコンテキストに送信相手との最新のメッセージ履歴を追加する
        return sorted(chat_partners.items(), key=lambda x: x[1], reverse=True)

class SendDirectMessageView(FormView):
    template_name = 'send_direct_message.html'
    form_class = DirectMessageForm

    def form_valid(self, form):
        recipient_id = self.kwargs['recipient_id']
        message = form.save(commit=False)
        message.sender = self.request.user
        message.recipient_id = recipient_id
        message.save()
        return redirect('inbox')  # 送信後はメッセージ一覧にリダイレクト

from django.views.generic import ListView
from .models import DirectMessage

class SentMessageView(ListView):
    template_name = 'sent_messages.html'
    model = DirectMessage
    context_object_name = 'sent_messages'

    def get_queryset(self):
        return DirectMessage.objects.filter(sender=self.request.user)   

class ChatView(ListView):
    template_name = 'chat.html'
    context_object_name = 'messages'

    def get_queryset(self):
        # ユーザーが送信したメッセージと受信したメッセージを取得
        sent_messages = DirectMessage.objects.filter(sender=self.request.user)
        received_messages = DirectMessage.objects.filter(recipient=self.request.user)
        # メッセージを日付でソートして結合
        all_messages = list(sent_messages) + list(received_messages)
        all_messages.sort(key=lambda x: x.timestamp)

       # チャット相手を特定する
        chat_partner = None
        if sent_messages.exists():
            chat_partner = sent_messages.first().recipient
        elif received_messages.exists():
            chat_partner = received_messages.first().sender
          
        # テンプレートに渡すコンテキストにチャット相手を追加する
        self.extra_context = {'chat_partner': chat_partner}
        

        return all_messages


#----DM作成ページ------

#----DM送信完了ページ------

#----DM受信完了ページ------

# class JobRegistView(CreateView,LoginRequiredMixin):
#     model = JobPost
#     template_name = "job_regist.html"
#     success_url = reverse_lazy("joblist:job_post_list")
#     fields = ['job_title','job_detail']
    
#     def form_valid(self, form):
#         # ログインしているユーザーを取得し、それを紐づける
#         form.instance.user = self.request.user
#         form.instance.user_name = self.request.user.username
#         return super().form_valid(form)

# class JobUpdateView(UpdateView,LoginRequiredMixin):
#     model = JobPost
#     template_name = "job_update.html"
#     success_url = reverse_lazy("joblist:job_post_list")
#     fields = ['job_title','job_detail']
#     pk_url_kwarg = 'pk'  # プライマリキーの名前を指定

# class JobDeleteView(DeleteView,LoginRequiredMixin):
#     model = JobPost
#     template_name = "job_delete.html"
#     success_url = reverse_lazy("joblist:job_post_list")
#     fields = ['job_title','job_detail']
#     pk_url_kwarg = 'pk'  # プライマリキーの名前を指定

