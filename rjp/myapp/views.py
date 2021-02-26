from django.shortcuts import render


def index_view(request):
    return render(request, "index.html", {})


def index_view_2(request):
    return render(request, "index.html", {})


def index_2_view(request):
    return render(request, "index2.html", {})


def index_3_view(request):
    return render(request, "index3.html", {})


def index_4_view(request):
    return render(request, "index4.html", {})


def html404(request):
    return render(request, "404.html", {})


def about_us(request):
    return render(request, "about-us.html", {})


def add_resume(request):
    return render(request, "add-resume.html", {})


def blog_grid_sidebar(request):
    return render(request, "blog-grid-sidebar.html", {})


def blog_single_sidebar(request):
    return render(request, "blog-single-sidebar.html", {})


def blog_single(request):
    return render(request, "blog-single.html", {})


def bookmarked(request):
    return render(request, "bookmarked.html", {})


def browse_categories(request):
    return render(request, "browse-categories.html", {})


def browse_jobs(request):
    return render(request, "browse-jobs.html", {})


def browse_resumes(request):
    return render(request, "browse-resumes.html", {})


def change_password(request):
    return render(request, "change-password.html", {})


def contact(request):
    return render(request, "contact.html", {})


def faq(request):
    return render(request, "faq.html", {})


def job_alerts(request):
    return render(request, "job-alerts.html", {})


def job_details(request):
    return render(request, "job-details.html", {})


def job_list(request):
    return render(request, "job-list.html", {})


def mail_success(request):
    return render(request, "mail-success.html", {})


def manage_applications(request):
    return render(request, "manage-applications.html", {})


def manage_jobs(request):
    return render(request, "manage-jobs.html", {})


def manage_resumes(request):
    return render(request, "manage-resumes.html", {})


def news_standard(request):
    return render(request, "news-standard.html", {})


def notifications(request):
    return render(request, "notifications.html", {})


def popper(request):
    return render(request, "popper.html", {})


def post_job(request):
    return render(request, "post-job.html", {})


def pricing(request):
    return render(request, "pricing.html", {})


def privacy_policy(request):
    return render(request, "privacy-policy.html", {})


def resume(request):
    return render(request, "resume.html", {})


def terms_conditions(request):
    return render(request, "terms-conditions.html", {})