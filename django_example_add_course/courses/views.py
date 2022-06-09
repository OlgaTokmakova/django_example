from .models import Course, Lesson
from django.views.generic import ListView, DetailView, CreateView

from courses.forms import CourseAddForm


class HomePage(ListView):
    model = Course
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница сайта'
        return ctx


class CourseDetailPage(DetailView):
    model = Course
    template_name = 'courses/course-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(CourseDetailPage, self).get_context_data(**kwargs)
        ctx['title'] = Course.objects.filter(slug=self.kwargs['slug']).first()
        ctx['lessons'] = Lesson.objects.filter(course=ctx['title']).order_by('number')
        # print(ctx['lessons'].query)
        return ctx


class LessonDetailPage(DetailView):
    model = Course
    template_name = 'courses/lessons-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(LessonDetailPage, self).get_context_data(**kwargs)

        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        lesson = list(Lesson.objects.filter(course=course).filter(slug=self.kwargs['lesson_slug']).values())

        #print(lesson)
        ctx['title'] = lesson[0]['title']
        ctx['desc'] = lesson[0]['description']
        ctx['video'] = lesson[0]['video_url'].split("=")[1]
        return ctx


class CourseAdd(CreateView):
    model = Course
    template_name = 'courses/add_course.html'
    form_class = CourseAddForm

    def get_context_data(self, **kwards):
        ctx = super(CourseAdd, self).get_context_data(**kwards)

        ctx['title'] = 'Добавление нового курса'
        ctx['btn_text'] = 'Добавить'
        return ctx

