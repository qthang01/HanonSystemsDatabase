from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView 
from .models import *
from .tables import *
from .forms import *
from .filters import *
from django.shortcuts import render
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django_tables2 import MultiTableMixin
from django.views.generic.base import TemplateView
from django.views.generic.detail import SingleObjectMixin
from datetime import datetime
from datetime import timedelta
from django.utils import timezone
from django.http import HttpResponse
from django.db.models import Q
import math

from .models import Test
from .forms import TestUpdateForm
from .tables import TestTable
from .filters import TestFilter
from django.core.paginator import Paginator



class LaptopListView(SingleTableMixin,  CreateView, FilterView):

    model = Laptop
    table_class = LaptopTable
    template_name = 'html/laptops.html'
    filterset_class = LaptopFilter
    form_class = LaptopForm
    success_url = '/database/Laptop'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Laptop"))
    def get_table_pagination(self, request):
        return False

class UpdateTableViewLaptop(SingleTableMixin,  UpdateView):
    
    model = Laptop
    form_class = LaptopForm
    template_name = 'html/update.html'
    success_url = '/database/Laptop'



def delete_Laptop(request, pk):

    Laptop.objects.filter(laptop_id=pk).delete()

    return HttpResponseRedirect(reverse("Laptop"))


class Test_HarnessListView(SingleTableMixin,  CreateView, FilterView):

    model = Test_Harness
    table_class = Test_HarnessTable
    template_name = 'html/Test_Harness.html'
    filterset_class = Test_HarnessFilter
    form_class = Test_HarnessForm
    success_url = '/database/Test_Harness'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Test_Harness"))
    def get_table_pagination(self, request):
        return False

class UpdateTableViewTest_Harness(SingleTableMixin,  UpdateView):
    
    model = Test_Harness
    form_class = Test_HarnessForm
    template_name = 'html/update.html'
    success_url = '/database/Test_Harness'



def delete_Test_Harness(request, pk):

    Test_Harness.objects.filter(id=pk).delete()

    return HttpResponseRedirect(reverse("Test_Harness"))

class Test_DUTListView(SingleTableMixin,  CreateView, FilterView):

    model = Test_DUT
    table_class = Test_DUTTable
    template_name = 'html/Test_DUT.html'
    filterset_class = Test_DUTFilter
    form_class = Test_DUTForm
    success_url = '/database/Test_DUT'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Test_DUT"))
    def get_table_pagination(self, request):
        return False

class UpdateTableViewTest_DUT(SingleTableMixin,  UpdateView):
    
    model = Test_DUT
    form_class = Test_DUTForm
    template_name = 'html/update.html'
    success_url = '/database/Test_DUT'



def delete_Test_DUT(request, pk):

    Test_DUT.objects.filter(id=pk).delete()

    return HttpResponseRedirect(reverse("Test_DUT"))


class Technician_SkillListView(SingleTableMixin,  CreateView, FilterView):

    model = Technician_Skill
    table_class = Technician_SkillTable
    template_name = 'html/technician_skills.html'
    filterset_class = Technician_SkillFilter
    form_class = Technician_SkillForm
    success_url = '/database/Technician_Skill'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Technician_Skill"))
    def get_table_pagination(self, request):
        return False

class UpdateTableViewTechnician_Skill(SingleTableMixin,  UpdateView):
    
    model = Technician_Skill
    form_class = Technician_SkillForm
    template_name = 'html/update.html'
    success_url = '/database/Technician_Skill'



def delete_Technician_Skill(request, pk):

    Technician_Skill.objects.filter(id=pk).delete()

    return HttpResponseRedirect(reverse("Technician_Skill"))


class TestMapListView(SingleTableMixin,  CreateView, FilterView):

    model = TestMap
    table_class = TestMapTable
    template_name = 'html/test_map.html'
    filterset_class = TestMapFilter
    form_class = TestMapForm
    success_url = '/database/TestMap'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("TestMap"))
    def get_table_pagination(self, request):
        return False

class UpdateTableViewTestMap(SingleTableMixin,  UpdateView):
    
    model = TestMap
    form_class = TestMapForm
    template_name = 'html/update.html'
    success_url = '/database/TestMap'



def delete_TestMap(request, pk):

    TestMap.objects.filter(test_map_id=pk).delete()

    return HttpResponseRedirect(reverse("TestMap"))


class Test_ChamberListView(SingleTableMixin,  CreateView, FilterView):

    model = Test_Chamber
    table_class = Test_ChamberTable
    template_name = 'html/index.html'
    filterset_class = Test_ChamberFilter
    form_class = Test_ChamberForm
    success_url = '/database/Test_Chamber'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Test_Chamber"))
    def get_table_pagination(self, request):
        return False

class UpdateTableViewTest_Chamber(SingleTableMixin,  UpdateView):
    
    model = Test_Chamber
    form_class = Test_ChamberForm
    template_name = 'html/update.html'
    success_url = '/database/Test_Chamber'



def delete_Test_Chamber(request, pk):

    Test_Chamber.objects.filter(id=pk).delete()

    return HttpResponseRedirect(reverse("Test_Chamber"))



class Program_CageListView(SingleTableMixin,  CreateView, FilterView):

    model = Program_Cage
    table_class = Program_CageTable
    template_name = 'html/index.html'
    filterset_class = Program_CageFilter
    form_class = Program_CageForm
    success_url = '/database/Program_Cage'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Program_Cage"))
    def get_table_pagination(self, request):
        return False

class UpdateTableViewProgram_Cage(SingleTableMixin,  UpdateView):
    
    model = Program_Cage
    form_class = Program_CageForm
    template_name = 'html/update.html'
    success_url = '/database/Program_Cage'



def delete_Program_Cage(request, pk):

    Program_Cage.objects.filter(id=pk).delete()

    return HttpResponseRedirect(reverse("Program_Cage"))



class Program_DARListView(SingleTableMixin,  CreateView, FilterView):

    model = Program_DAR
    table_class = Program_DARTable
    template_name = 'html/DAR_program.html'
    filterset_class = Program_DARFilter
    form_class = Program_DARForm
    success_url = '/database/Program_DAR'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Program_DAR"))
    def get_table_pagination(self, request):
        return False

class UpdateTableViewProgram_DAR(SingleTableMixin,  UpdateView):
    
    model = Program_DAR
    form_class = Program_DARForm
    template_name = 'html/update.html'
    success_url = '/database/Program_DAR'



def delete_Program_DAR(request, pk):

    Program_DAR.objects.filter(id=pk).delete()

    return HttpResponseRedirect(reverse("Program_DAR"))


class Program_FluidListView(SingleTableMixin,  CreateView, FilterView):

    model = Program_Fluid
    table_class = Program_FluidTable
    template_name = 'html/Program_fluid.html'
    filterset_class = Program_FluidFilter
    form_class = Program_FluidForm
    success_url = '/database/Program_Fluid'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Program_Fluid"))
    def get_table_pagination(self, request):
        return False

class UpdateTableViewProgram_Fluid(SingleTableMixin,  UpdateView):
    
    model = Program_Fluid
    form_class = Program_FluidForm
    template_name = 'html/update.html'
    success_url = '/database/Program_Fluid'



def delete_Program_Fluid(request, pk):

    Program_Fluid.objects.filter(id=pk).delete()

    return HttpResponseRedirect(reverse("Program_Fluid"))





class DARChannelListView(SingleTableMixin,  CreateView, FilterView):

    model = DARChannel
    table_class = DARChannelTable
    template_name = 'html/index.html'
    filterset_class = DARChannelFilter
    form_class = DARChannelForm
    success_url = '/database/DARChannel'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("DARChannel"))
    def get_table_pagination(self, request):
        return False

class UpdateTableViewDARChannel(SingleTableMixin,  UpdateView):
    
    model = DARChannel
    form_class = DARChannelForm
    template_name = 'html/update.html'
    success_url = '/database/DARChannel'



def delete_DARChannel(request, pk):

    DARChannel.objects.filter(channel_id=pk).delete()

    return HttpResponseRedirect(reverse("DARChannel"))



class FluidListView(SingleTableMixin,  CreateView, FilterView):

    model = Fluid
    table_class = FluidTable
    template_name = 'html/test_fluids.html'
    filterset_class = FluidFilter
    form_class = FluidForm
    success_url = '/database/Fluid'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Fluid"))
    def get_table_pagination(self, request):
        return False

class UpdateTableViewFluid(SingleTableMixin,  UpdateView):
    
    model = Fluid
    form_class = FluidForm
    template_name = 'html/update.html'
    success_url = '/database/Fluid'



def delete_Fluid(request, pk):

    Fluid.objects.filter(fluid_id=pk).delete()

    return HttpResponseRedirect(reverse("Fluid"))



class TechnicianListView(SingleTableMixin,  CreateView, FilterView):

    model = Technician
    table_class = TechnicianTable
    template_name = 'html/technician.html'
    filterset_class = TechnicianFilter
    form_class = TechnicianForm
    success_url = '/database/Technician'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Technician"))
    def get_table_pagination(self, request):
        return False

class UpdateTableViewTechnician(SingleTableMixin,  UpdateView):
    
    model = Technician
    table_class = TechnicianTable
    form_class = TechnicianForm
    template_name = 'html/update.html'
    success_url = '/database/Technician'



def delete_Technician(request, pk):

    Technician.objects.filter(technician_id=pk).delete()

    return HttpResponseRedirect(reverse("Technician"))


class TestTypeListView(SingleTableMixin,  CreateView, FilterView):

    model = TestType
    table_class = TestTypeTable
    template_name = 'html/index.html'
    filterset_class = TestTypeFilter
    form_class = TestTypeForm
    success_url = '/database/TestType'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("TestType"))
    def get_table_pagination(self, request):
        return False

class UpdateTableViewTestType(SingleTableMixin,  UpdateView):
    
    model = TestType
    form_class = TestTypeForm
    template_name = 'html/update.html'
    success_url = '/database/TestType'



def delete_TestType(request, pk):

    TestType.objects.filter(test_type_id=pk).delete()

    return HttpResponseRedirect(reverse("TestType"))


class LabListView(SingleTableMixin,  CreateView, FilterView):

    model = Lab
    table_class = LabTable
    template_name = 'html/labs.html'
    filterset_class = LabFilter
    form_class = LabForm
    success_url = '/database/Lab'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Lab"))
    def get_table_pagination(self, request):
        return False

class UpdateTableViewLab(SingleTableMixin,  UpdateView):
    
    model = Lab
    form_class = LabForm
    template_name = 'html/update.html'
    success_url = '/database/Lab'



def delete_Lab(request, pk):

    Lab.objects.filter(lab_id=pk).delete()

    return HttpResponseRedirect(reverse("Lab"))


class SkillListView(SingleTableMixin,  CreateView, FilterView):

    model = Skill
    table_class = SkillTable
    template_name = 'html/index.html'
    filterset_class = SkillFilter
    form_class = SkillForm
    success_url = '/database/Skill'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Skill"))
    def get_table_pagination(self, request):
        return False

class UpdateTableViewSkill(SingleTableMixin,  UpdateView):
    
    model = Skill
    form_class = SkillForm
    template_name = 'html/update.html'
    success_url = '/database/Skill'



def delete_Skill(request, pk):

    Skill.objects.filter(skill_id=pk).delete()

    return HttpResponseRedirect(reverse("Skill"))

class HarnessListView(SingleTableMixin,  CreateView, FilterView):

    model = Harness
    table_class = HarnessTable
    template_name = 'html/harness.html'
    filterset_class = HarnessFilter
    form_class = HarnessForm
    success_url = '/database/Harness'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Harness"))
    def get_table_pagination(self, request):
        return False

class UpdateTableViewHarness(SingleTableMixin,  UpdateView):
    
    model = Harness
    form_class = HarnessForm
    template_name = 'html/update.html'
    success_url = '/database/Harness'



def delete_Harness(request, pk):

    Harness.objects.filter(harness_id=pk).delete()

    return HttpResponseRedirect(reverse("Harness"))



class ProgramListView(SingleTableMixin,  CreateView, FilterView):

    model = Program
    table_class = ProgramTable
    template_name = 'html/programs.html'
    filterset_class = ProgramFilter
    form_class = ProgramForm
    success_url = '/database/program'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("program"))
    def get_table_pagination(self, request):
        return False

class CageListView(SingleTableMixin,  CreateView, FilterView):

    model = Cage
    table_class = CageTable
    template_name = 'html/cage.html'
    filterset_class = CageFilter
    form_class = CageForm
    success_url = '/database/cage'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("cage"))
    def get_table_pagination(self, request):
        return False
    
class UpdateTableViewCage(SingleTableMixin,  UpdateView):
    
    model = Cage
    form_class = CageForm
    template_name = 'html/update cage.html'
    success_url = '/database/cage'



def delete_cage(request, pk):

    Cage.objects.filter(cage_id=pk).delete()

    return HttpResponseRedirect(reverse("cage"))
    


class ChamberListView(SingleTableMixin,  CreateView, FilterView):

    model = Chamber
    table_class = ChamberTable
    template_name = 'html/Chamber.html'
    filterset_class = ChamberFilter
    form_class = ChamberForm
    success_url = '/database/Chamber'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Chamber"))
    def get_table_pagination(self, request):
        return False
    
class UpdateTableViewChamber(SingleTableMixin,  UpdateView):
    
    model = Chamber
    form_class = ChamberForm
    template_name = 'html/update Chamber.html'
    success_url = '/database/Chamber'



def delete_Chamber(request, pk):

    Chamber.objects.filter(chamber_id=pk).delete()

    return HttpResponseRedirect(reverse("Chamber"))




class UpdateTableViewProgram(SingleTableMixin,  UpdateView):
    
    model = Program
    table_class = ProgramTable
    form_class = ProgramForm
    template_name = 'html/update.html'
    success_url = '/database/program'



def delete_program(request, pk):

    Program.objects.filter(program_id=pk).delete()

    return HttpResponseRedirect(reverse("program"))


class DarListView(SingleTableMixin,  CreateView, FilterView):

    model = DAR
    table_class = DarTable
    template_name = 'html/Dar.html'
    filterset_class = DarFilter
    form_class = DarForm
    success_url = '/database/Dar'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Dar"))
    def get_table_pagination(self, request):
        return False
    
class UpdateTableViewDar(SingleTableMixin,  UpdateView):
    
    model = DAR
    form_class = DarForm
    template_name = 'html/update Dar.html'
    success_url = '/database/Dar'



def delete_Dar(request, pk):

    DAR.objects.filter(dar_id=pk).delete()

    return HttpResponseRedirect(reverse("Dar"))
    



class ProductListView(SingleTableMixin,  CreateView, FilterView):
    
    model = Product
    table_class = ProductTable
    template_name = 'html/product.html'
    filterset_class = ProductFilter
    form_class = ProductForm
    success_url = '/database/product'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("product"))
    def get_table_pagination(self, request):
        return False

class UpdateTableViewProduct(SingleTableMixin,  UpdateView):
    
    model = Product
    template_name = 'html/update_prod.html'
    form_class = ProductForm
    success_url = '/database/product'



def delete_item_product(request, pk):

    Product.objects.filter(product_id=pk).delete()

    return HttpResponseRedirect(reverse("product"))

# class TestListView(SingleTableMixin, CreateView, FilterView):
    
#     model = Test
#     table_class = TestTable
#     template_name = 'html/test.html'
#     success_url = '/database/tests'
#     filterset_class = TestFilter
#     form_class = TestForm
#     def get_table_pagination(self, request):
#         return False

# class UpdateTableViewTest(SingleTableMixin,  UpdateView, FilterView):
    
    
#     model = Test
#     template_name = 'html/update_test.html'
#     form_class = TestUpdateForm
#     # template_name_suffix = 'html/index.html'
#     # fields = '__all__'
#     filterset_class = TestFilter
#     success_url = '/database/tests'

from django.shortcuts import render, get_object_or_404, redirect
from django_tables2.views import SingleTableMixin
from django.views.generic import CreateView, UpdateView
from django_filters.views import FilterView
from .models import Test
from .forms import TestForm, TestUpdateForm
from .tables import TestTable
from .filters import TestFilter

class TestListView(SingleTableMixin, CreateView, FilterView):
    model = Test
    table_class = TestTable
    template_name = 'html/test.html'
    success_url = '/database/tests'
    filterset_class = TestFilter
    form_class = TestForm

    def get_table_pagination(self, request):
        return False
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tests = self.get_queryset()
        paginator = Paginator(tests, 10)
        page = self.request.GET.get('page')
        context['page_obj'] = paginator.get_page(page)
        context['is_paginated'] = True
        return context

class UpdateTableViewTest(SingleTableMixin, UpdateView, FilterView):
    model = Test
    template_name = 'html/update_test.html'
    form_class = TestUpdateForm
    filterset_class = TestFilter
    success_url = '/database/tests'
    table_class = TestTable

    def get_queryset(self):
        return Test.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 设置 object_list，这里使用 get_queryset() 获取查询集
        context['object_list'] = self.get_queryset()
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        test = Test.objects.get(pk=instance.pk)

        # 处理 supervisor_comments 字段
        if test.supervisor_comments in instance.supervisor_comments and test.supervisor_comments != instance.supervisor_comments:
            input = instance.supervisor_comments.replace("\n" + test.supervisor_comments, '')
            new_line = str(datetime.now().date()) + " " + input + "\n"
            new_comment = new_line + test.supervisor_comments
            instance.supervisor_comments = new_comment
        elif test.supervisor_comments == instance.supervisor_comments:
            pass
        else:
            position = instance.supervisor_comments.find("\n")
            new_line = str(datetime.now().date()) + " " + instance.supervisor_comments[:position + 1]
            new_comment = new_line + instance.supervisor_comments[position + 1:]
            instance.supervisor_comments = new_comment

        instance.save()

        # 更新相关的 ChamberLogInfo
        info, created = ChamberLogInfo.objects.get_or_create(test_id=instance.pk)
        info.comments = instance.supervisor_comments
        info.chamber_id = instance.chamber_id
        info.technician_id = instance.technician_id
        info.program_id = instance.program_id
        info.save()

        return super().form_valid(form)


def find(request, pk):
    try:
        p = ChamberLogInfo.objects.get(test_id=pk).pk
        # 这里你可以添加处理找到的对象的逻辑
    except ChamberLogInfo.DoesNotExist:
        # 如果对象不存在，返回一个友好的错误页面或消息
        return render(request, 'error_page.html', {'message': 'ChamberLogInfo with this test ID does not exist.'})
    # 如果对象存在，继续处理你的逻辑
    return HttpResponseRedirect(reverse("ChamberLog", kwargs={'pk': p}))


def delete_item_test(request, pk):

    Test.objects.filter(test_id=pk).delete()

    items = Test.objects.all()

    context = {
    'items': items
    }
    return HttpResponseRedirect(reverse("test"))

def clone_item(request, pk):

    obj = Test.objects.get(test_id = pk)
    obj.pk = None
    obj.created = timezone.now()
    obj.save()
    ch = ChamberLogInfo(chamber_id = obj.chamber_id, program_id = obj.program_id, technician_id = obj.technician_id, test_id = Test.objects.get(pk = obj.pk),
                                pretest_inspection_and_photo=None,
                                setup_photo=None,
                                humidity=None,
                                system_pressure=None,
                                voltage=None,
                                system_restriction_target=None,
                                system_restriction_record=None,
                                trial_run_record_and_process=None,
                                special_requirements=None,
                                comments = obj.supervisor_comments)

    ch.save()

    return HttpResponseRedirect(reverse("test"))



def clone_item1(request, pk):

    obj = Product.objects.get(product_id = pk)
    obj.pk = None
    obj.created = timezone.now()
    obj.save()

    return HttpResponseRedirect(reverse("product"))

def clone_item2(request, pk):

    obj = Program.objects.get(program_id = pk)
    obj.pk = None
    obj.created = timezone.now()
    obj.save()
    

    return HttpResponseRedirect(reverse("program"))



def children(request):
    test_type_id = request.body
    try:
        test_type_id = int(test_type_id)
    except:
        a = open("database/templates/html/children", "w")
        a.write("{\n")
        a.close()
        return HttpResponse()
    else:
        test_cham = Test_Chamber.objects.filter(test_type_id = test_type_id) #.order_by("targeted_start");
        a = open("database/templates/html/children", "w")
        a.write("{\n")
        a.close()
        a = open("database/templates/html/children", "a")
        for i in range(len(test_cham)):
            a.write(f'\"id{i}\": {{\"chamber_id\" : \"{test_cham[i].chamber_id.chamber_id}\"}}')
            if i != (len(test_cham)-1):
                a.write(",\n")
        a.write("\n}")
        a.close()
        return HttpResponse("product highligth compiled")
    
def children1(request):
    test_type_id = request.body
    try:
        test_type_id = int(test_type_id)
    except:
        a = open("database/templates/html/children", "w")
        a.write("{\n")
        a.close()
        return HttpResponse()
    else:
        test_cham = Test.objects.filter(test_id = test_type_id) #.order_by("targeted_start");
        a = open("database/templates/html/children", "w")
        a.write("{\n")
        a.close()
        a = open("database/templates/html/children", "a")
        for i in range(len(test_cham)):
            a.write(f'\"id{i}\": {{\"chamber_id\" : \"{test_cham[i].chamber_id.chamber_id}\"}}')
            if i != (len(test_cham)-1):
                a.write(",\n")
        a.write("\n}")
        a.close()
        return HttpResponse("product highligth compiled")
    
def getchildren(request):
    return render(request, "html/children")


def darchildren(request):
    program_id = request.body
    try:
        program_id = int(program_id)
    except:
        a = open("database/templates/html/children", "w")
        a.write("{\n")
        a.close()
        return HttpResponse()
    else:
        prog_dar = Program_DAR.objects.filter(program_id = program_id) #.order_by("targeted_start");
        prog_cage = Program_Cage.objects.filter(program_id = program_id)
        a = open("database/templates/html/children", "w")
        a.write("{\n")
        a.close()
        a = open("database/templates/html/children", "a")
        b = 0
        for i in range(len(prog_dar)):
            b = b+1
            a.write(f'\"id{i}\": {{\"dar_id\" : \"{prog_dar[i].dar_id.dar_id}\"}}')
            if i != (len(prog_dar)-1):
                a.write(",\n")
        if (len(prog_dar) > 0 and len(prog_cage) > 0):
            a.write(",\n")
        for i in range(len(prog_cage)):
            a.write(f'\"id{b}\": {{\"cage_id\" : \"{prog_cage[i].cage_id.cage_id}\"}}')
            b = b + 1
            if i != (len(prog_cage)-1):
                a.write(",\n")
        a.write("\n}")
        a.close()
        return HttpResponse("product highligth compiled")
    
def getdarchildren(request):
    return render(request, "html/children")

def chamber_schedule(request):
    chamber_id = request.body
    try:
        chamber_id = int(chamber_id)
    except:
        a = open("database/templates/html/chamber_schedule", "w")
        a.write("")
        a.close()
        return HttpResponse("No chamber selected")
    else:
        chamber_tests = Test.objects.filter(Q(scheduling = "current")|Q(scheduling = "upcoming")).filter(chamber_id = chamber_id).order_by("targeted_start")
        a = open("database/templates/html/chamber_schedule", "w")
        a.write("{\n")
        a.close()
       

        a = open("database/templates/html/chamber_schedule", "a")
        for i in range(len(chamber_tests)):
            a.write(f'\"booking{i}\": {{\"targeted_start\" : \"{chamber_tests[i].targeted_start}\", \"targeted_end\" : \"{chamber_tests[i].targeted_end}\",' 
                    + f'\"test_map_id\" : \"{chamber_tests[i].test_map_id.tr}\", \"product_id\" : \"{chamber_tests[i].product_id}\", \"test_type_id\" : \"{chamber_tests[i].test_type_id}\", \"program_id\" : '
                    + f'\"{chamber_tests[i].program_id}\", \"scheduling\" : \"{chamber_tests[i].scheduling}\"}},\n')
        
        a.write(f'\"chamber\": \"{Chamber.objects.get(chamber_id=chamber_id)}\"\n}}')
        a.close()
        return HttpResponse("Chamber schedule compiled")

def get_chamber_schedule(request):
    return render(request, "html/chamber_schedule")

def dar_schedule(request):
    dar_id = request.body
    try:
        dar_id = int(dar_id)
    except:
        a = open("database/templates/html/dar_schedule", "w")
        a.write("")
        a.close()
        return HttpResponse("No DAR selected")
    else:
        dar_tests = Test.objects.filter(Q(scheduling = "current")|Q(scheduling = "upcoming")).filter(dar_id = dar_id).order_by("targeted_start")
        a = open("database/templates/html/dar_schedule", "w")
        a.write("{\n")
        a.close()

        a = open("database/templates/html/dar_schedule", "a")
        for i in range(len(dar_tests)):
            a.write(f'\"booking{i}\": {{\"targeted_start\" : \"{dar_tests[i].targeted_start}\", \"targeted_end\" : \"{dar_tests[i].targeted_end}\",' 
                    + f'\"test_map_id\" : \"{dar_tests[i].test_map_id.tr}\", \"product_id\" : \"{dar_tests[i].product_id}\", \"test_type_id\" : \"{dar_tests[i].test_type_id}\", \"program_id\" : '
                    + f'\"{dar_tests[i].program_id}\", \"scheduling\" : \"{dar_tests[i].scheduling}\"}},\n')
        
        a.write(f'\"DAR\": \"{DAR.objects.get(dar_id=dar_id)}\"\n}}')
        a.close()
        return HttpResponse("DAR schedule compiled")

def get_dar_schedule(request):
    return render(request, "html/dar_schedule")

def cage_schedule(request):
    cage_id = request.body
    try:
        cage_id = int(cage_id)
    except:
        a = open("database/templates/html/cage_schedule", "w")
        a.write("")
        a.close()
        return HttpResponse("No cage selected")
    else:
        cage_tests = Test.objects.filter(Q(scheduling = "current")|Q(scheduling = "upcoming")).filter(cage_id = cage_id).order_by("targeted_start")
        a = open("database/templates/html/cage_schedule", "w")
        a.write("{\n")
        a.close()

        a = open("database/templates/html/cage_schedule", "a")
        for i in range(len(cage_tests)):
            a.write(f'\"booking{i}\": {{\"targeted_start\" : \"{cage_tests[i].targeted_start}\", \"targeted_end\" : \"{cage_tests[i].targeted_end}\",' 
                    + f'\"test_map_id\" : \"{cage_tests[i].test_map_id.tr}\", \"product_id\" : \"{cage_tests[i].product_id}\", \"test_type_id\" : \"{cage_tests[i].test_type_id}\", \"program_id\" : '
                    + f'\"{cage_tests[i].program_id}\", \"scheduling\" : \"{cage_tests[i].scheduling}\"}},\n')
        
        a.write(f'\"Cage\": \"{Cage.objects.get(cage_id=cage_id)}\"\n}}')
        a.close()
        return HttpResponse("Cage schedule compiled")

def get_cage_schedule(request):
    return render(request, "html/cage_schedule")



class ChamberLogInfoListView(SingleTableMixin, CreateView, FilterView):
    
    model = ChamberLogInfo
    table_class = ChamberLogInfoTable
    template_name = 'html/ChamberLogInfo.html'
    success_url = '/database/ChamberLogInfo'
    filterset_class = ChamberLogInfoFilter
    form_class = ChamberLogInfoForm
    def get_table_pagination(self, request):
        return False

    

class UpdateTableViewChamberLogInfo(SingleTableMixin,  UpdateView):
    model = ChamberLogInfo
    template_name = 'html/update_ChamberLogInfo.html'
    form_class = ChamberLogInfoForm
    # template_name_suffix = 'html/index.html'
    # fields = '__all__'
    def get_success_url(self):
        return reverse('ChamberLog', kwargs={'pk': self.kwargs.get('pk')})



def delete_item_ChamberLogInfo(request, pk):

    ChamberLogInfo.objects.filter(id=pk).delete()

    items = ChamberLogInfo.objects.all()

    context = {
    'items': items
    }

    return HttpResponseRedirect(reverse("ChamberLogInfo"))

def clone_item3(request, pk):

    obj = ChamberLogInfo.objects.get(id = pk)
    obj.pk = None
    obj.created = timezone.now()
    obj.save()

    return HttpResponseRedirect(reverse("ChamberLogInfo"))

class ChamberLogView(SingleTableMixin, CreateView, FilterView):
    template_name = 'html/ChamberLog.html'
    model = ChamberLog
    table_class = ChamberLogTable
    form_class = ChamberLogForm
    filterset_class = ChamberLogFilter
    
    def get_queryset(self, *args, **kwargs):
        return ChamberLog.objects.filter(log_id = self.kwargs.get('pk'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ChamberLogInfo'] = ChamberLogInfo.objects.filter(pk = self.kwargs.get('pk'))
        context['Comments'] = ChamberLogInfo.objects.filter(pk = self.kwargs.get('pk'))[0].comments.replace("\n", "<br>")
        return context
    
    def get_success_url(self):
        return reverse('ChamberLog', kwargs={'pk': self.kwargs.get('pk')})
    
    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("ChamberLog", kwargs={'pk': self.kwargs.get('pk')}))
    def get_table_pagination(self, request):
        return False

def delete_item_ChamberLog(request, pk):
    item = ChamberLog.objects.get(id = pk).log_id.id

    ChamberLog.objects.filter(id=pk).delete()

   

    return HttpResponseRedirect(reverse("ChamberLog", kwargs={'pk': item}))

def clone_item4(request, pk):

    obj = ChamberLog.objects.get(id = pk)
    obj.pk = None
    obj.save()

    return  HttpResponseRedirect(reverse('ChamberLog', kwargs={'pk': obj.log_id.id}))



def menu(request):
    return render(request, "html/menu.html")



def hours_calculations(request):
    return render(request, "html/hours_calculations.html")

def calculate(request):
    a = open("database/static/database/programhours.csv", "w")
    a.write("")
    a.write("Chamber,Program,Running,Setup,Waiting for product,Stopped,Total Operable Hours,Billing Category\n")
    a.close()
    dates = str(request.body)
    first = dates.find("'")
    last = dates.find("'", first +1)
    dates = dates[first+1: last]
    dates = dates.split(",")
    dates[0] = datetime.strptime(dates[0], "%Y-%m-%d")                  #converting date string to date object
    dates[1] = datetime.strptime(dates[1], "%Y-%m-%d")
    program_hours = {}
    
    all_logs = ChamberLog.objects.filter(timestamp__gte = dates[0]).filter(timestamp__lte = dates[1])    #getting all logs in the specified time period
    chambers = Chamber.objects.all()
    for chamber in chambers:
        chamber_name = chamber.chamber_name
        max_hours = chamber.max_daily_hours  #getting the max hour of the current chamber
        operable_hours = (dates[1]-dates[0]).days*max_hours #getting total time in period
        chamber_logs = all_logs.filter(chamber_id = chamber.chamber_id)        #getting logs of current chamber

        tests_checked= []       #to skip over tests that have already been accounted
        
        program_hours[chamber_name] = {}
        
        for test in chamber_logs:
            if test.log_id.test_id in tests_checked:            #only assessing distinct tests
                continue
            else:
                tests_checked.append(test.log_id.test_id)
                used_hours = {}     #to keep track of the operable hours used for a certain day
                
            test_logs = chamber_logs.filter(log_id__test_id= test.log_id.test_id).order_by("timestamp")       #getting chamber logs that belong to current test
            program_name = test.log_id.test_id.program_id.program_name
            
            stop = False
            logs = test_logs.filter(circuit_number = test_logs[0].circuit_number).order_by("timestamp")
            
            try:                #checking for log of test before the selected time period
                previous_log = ChamberLog.objects.filter(log_id__test_id= logs[0].log_id.test_id).filter(chamber_id= logs[0].chamber_id).filter(timestamp__lt = dates[0]).latest("timestamp")
            except:
                previous_log=0
            first_of_test = False
            
            while stop == False:
                for log in logs:
                    if log == logs[0]:  #in case this is the leading log, check if the previous log's present
                        if previous_log == 0:           #case 1:first log of test
                            first_log = True
                            overlap = False
                            first_of_test = True
                        else:    
                            try:
                                last_log = ChamberLog.objects.filter(log_id__test_id= log.log_id.test_id).filter(chamber_id= log.chamber_id).filter(circuit_number = log.circuit_number).filter(timestamp__lt = log.timestamp).latest("timestamp")
                            except:
                                first_log = True               #case 2:no previous log in current circuit, but there is a previous log from another circuit
                                switch_date = str(previous_log.timestamp.day) + "/" + str(previous_log.timestamp.month) + "/" + str(previous_log.timestamp.year)
                                try:                #checking used hours on the day of the previous log
                                    used = used_hours[switch_date]
                                except:
                                    used = 0 
                                time_adjustment = previous_log.timestamp - timedelta(0,(max_hours-used)*60*60)
                                in_between = (log.timestamp - time_adjustment).days*max_hours + (log.timestamp - time_adjustment).seconds/60/60
                                
                                if in_between >= log.total_hours:           #case 2.1: if running hours recorded overlaps the hours up until the previous log
                                    overlap = False
                                else:
                                    overlap = True
                                    no_overlap = log.timestamp - previous_log.timestamp      
                            else:                       #case 3: there is a previous log of the circuit, as well as a previous log that could belong to any circuit (these could be the same thing)
                                first_log = False  
                                if previous_log.timestamp > last_log.timestamp:     #checking to see if last log is before or after where we switched, if this is the first log of the time period, "try" makes sure that value 0 doesn't cause errors
                                    overlap = True              #case 3.1: there is overlap between these two logs
                                    no_overlap = log.timestamp - previous_log.timestamp
                                    switch_date = str(previous_log.timestamp.day) + "/" + str(previous_log.timestamp.month) + "/" + str(previous_log.timestamp.year)
                                    try:
                                        used = used_hours[switch_date]
                                    except:
                                        used = 0
                                else:                           #case 3.2: there is no overlap between these two logs
                                    overlap = False     
                                previous_log = last_log                        #make the previous log the one we searched for, indicate that there is a log before current one.
                                
                                
                    
                    if first_log == True:           #Case 1 and 2's:
                        date = str(log.timestamp.day) + "/" + str(log.timestamp.month) + "/" + str(log.timestamp.year)
                        if first_of_test == True:
                            running_hours = log.total_hours
                            status_hours = 0
                            first_of_test = False
                        else:
                            if overlap == False:
                                running_hours = log.total_hours                         #Step 1: calculating hours
                                try:
                                    status_hours = math.ceil(in_between - running_hours)
                                except:
                                    status_hours = 0
                            else:         #Case 2's:
                                running_hours = math.ceil(in_between)
                                status_hours = 0
                                overlap = False
                            
                        if running_hours < max_hours:                           #updating used hours
                            used_hours[date] = running_hours
                        else:
                            used_hours[date] = max_hours        

                        
                        if program_name not in program_hours[chamber_name].keys():                                #Step 2: updating program hours, for logs that lead a series of logs
                            program_hours[chamber_name][program_name]={}
                            program_hours[chamber_name][program_name]["running"] = running_hours 
                            program_hours[chamber_name][program_name]["stopped"] = status_hours
                            program_hours[chamber_name][program_name]["operable"] = operable_hours
                            program_hours[chamber_name][program_name]["billing category"] = chamber.billing_category
                        else:               #program has been registered
                            program_hours[chamber_name][program_name]["running"] = program_hours[chamber_name][program_name]["running"] + running_hours
                            program_hours[chamber_name][program_name]["stopped"] = program_hours[chamber_name][program_name]["stopped"] + status_hours
                        
                        first_log= False
                        previous_log = log
                        #print("first log in new series:")
                        #print(program_hours)
                        
                        
                        if log.status == "stopped" or log == logs[len(logs)-1]:        #when the current log is the last of the circuit logs, or the stretch of logs is stopped.
                            try:
                                next_log = test_logs.filter(timestamp__gt = log.timestamp).earliest("timestamp")
                            except:
                                stop = True
                                break
                            else:
                                logs = test_logs.filter(timestamp__gt = log.timestamp).filter(circuit_number = next_log.circuit_number).order_by("timestamp")
                                break
                        continue
                    
                    
                    else:                                                                   #Case 3's:                  
                        running_hours = log.total_hours - previous_log.total_hours          #Step 1: calculating hours between two subsequent logs
                        current_timestamp = log.timestamp
                        previous_timestamp = previous_log.timestamp
                        date = str(current_timestamp.day) + "/" + str(current_timestamp.month) + "/" + str(current_timestamp.year)
                        previous_date = str(previous_timestamp.day) + "/" + str(previous_timestamp.month) + "/" + str(previous_timestamp.year) 
                        
                        if date == previous_date:                                                       #Case 1: when two subsequent logs are on the same day
                            in_between = (current_timestamp - previous_timestamp).seconds/60/60     #only time to be accounted for is that between two logs
                            try:
                                available = max_hours - used_hours[date]            #checking operable hours available
                            except:
                                available = max_hours
                                
                            if available > in_between:
                                status_hours = math.ceil(in_between - running_hours)
                            else:
                                status_hours = available - running_hours
                                
                            if status_hours < 0:                    #in case the assumption of max daily hours is incorrect, this prevents subtractions from previously summed status hours
                                status_hours = 0
                                
                            if date in used_hours:
                                if previous_log.status == "running" or previous_log.status == "stopped":
                                    used_hours[date] = used_hours[date] + running_hours
                                else:
                                    used_hours[date] = used_hours[date] + running_hours + status_hours
                            else:
                                if previous_log.status == "running" or previous_log.status == "stopped":
                                    used_hours[date] = running_hours
                                else:
                                    used_hours[date] = running_hours + status_hours
                                    
                            
                                  
                        else:                                                       #Case 2: when two subsequent logs are on different dates
                            endofday_previous = datetime(previous_timestamp.year, previous_timestamp.month, previous_timestamp.day, 23, 59, 59, 0)
                            startofday_current = datetime(current_timestamp.year, current_timestamp.month, current_timestamp.day, 0, 0, 0, 0)
                            beginning_period = (endofday_previous - previous_timestamp).seconds/60/60
                            in_between = (startofday_current - endofday_previous).days*max_hours
                            end_period = (current_timestamp - startofday_current).seconds/60/60
                            try:
                                available = max_hours - used_hours[previous_date]
                            except:
                                available = max_hours
                                
                            if available > beginning_period:                #adding duration of first period
                                occupied_beginning = beginning_period
                            else:
                                occupied_beginning = available
                            
                            if max_hours > end_period:                      #adding duration of end period
                                occupied_end = end_period 
                            else:
                                occupied_end = max_hours
                                                                         
                            status_hours = math.ceil(occupied_beginning + in_between +occupied_end - running_hours)         #adding duration of in between period

                            if status_hours < 0:                    #in case the assumption of max daily hours is incorrect, this prevents subtractions from previously summed status hours
                                status_hours = 0

                            if occupied_beginning + in_between < running_hours:                                             #updating used hours
                                if previous_log.status == "running":                                                    #Case 1: chamber run time can stretch from last log into the day of current log
                                    used_hours[date] = math.ceil(running_hours - occupied_beginning - in_between)
                                else:
                                    used_hours[date] = occupied_end
                            else:                                                                       #Case 2: chamber run time doesn't stretch from last log into the day of current log
                                if previous_log.status == "running":
                                    used_hours[date] = 0
                                elif previous_log.status == "stopped":
                                    if running_hours < occupied_end:
                                        used_hours[date] = running_hours
                                    else:
                                        used_hours[date] = occupied_end
                                else:
                                    used_hours[date] = occupied_end
                                    
                            
                            
                        if overlap == True:
                            grey_period = no_overlap.days*max_hours + no_overlap.seconds/60/60 - used
                            if running_hours >= grey_period:
                                running_hours = math.ceil(grey_period)
                                status_hours = 0
                            else:
                                status_hours = math.ceil(grey_period-running_hours)
                            overlap == False
                                

                    if program_name not in program_hours[chamber_name].keys():                                #Step 2: updating program hours
                        program_hours[chamber_name][program_name]={}
                        program_hours[chamber_name][program_name]["running"] = running_hours
                        program_hours[chamber_name][program_name]["stopped"] = 0
                        program_hours[chamber_name][program_name]["operable "] = operable_hours
                        program_hours[chamber_name][program_name]["billing category"] = chamber.billing_category
                        if previous_log.status == "running":
                            program_hours[chamber_name][program_name]["stopped"] = program_hours[chamber_name][program_name]["stopped"] + status_hours
                        else:
                            program_hours[chamber_name][program_name][previous_log.status] = status_hours 

                    else:                                                                   
                        program_hours[chamber_name][program_name]["running"] = program_hours[chamber_name][program_name]["running"] + running_hours
                        if previous_log.status not in program_hours[chamber_name][program_name].keys():
                            program_hours[chamber_name][program_name][previous_log.status] = status_hours
                        else:
                            if previous_log.status == "running":
                                program_hours[chamber_name][program_name]["stopped"] = program_hours[chamber_name][program_name]["stopped"] + status_hours
                            else:
                                program_hours[chamber_name][program_name][previous_log.status] = program_hours[chamber_name][program_name][previous_log.status] + status_hours                             
                            
                    previous_log = log
                    #print(program_hours)
                    
                    if log.status == "stopped" or log == logs[len(logs)-1]:        #Step 3: Checking switching conditions
                        try:
                            next_log = test_logs.filter(timestamp__gt = log.timestamp).earliest("timestamp")
                        except:
                            stop = True
                            break
                        else:
                            logs = test_logs.filter(timestamp__gt = log.timestamp).filter(circuit_number = next_log.circuit_number).order_by("timestamp")
                            break
    #print(program_hours)              
    #write csv file for program hours:
    a = open("database/static/database/programhours.csv", "a")
    for i in program_hours:
        for x in program_hours[i]:
            a.write(f'{i},')
            a.write(f'{x},')
            try:
                a.write(f'{program_hours[i][x]["running"]},')
            except:
                a.write("0,")
            
            try: 
                a.write(f'{program_hours[i][x]["setup"]},')
            except:
                a.write("0,")
            
            try:
                a.write(f'{program_hours[i][x]["waiting for product"]},')
            except:
                a.write("0,")
            
            try:
                a.write(f'{program_hours[i][x]["stopped"]},')
            except:
                a.write("0,")

            a.write(f'{program_hours[i][x]["operable"]},')    
            a.write(f'{program_hours[i][x]["billing category"]}\n')

    a.close()  
    return HttpResponse("hours compiled");

def hours_download(request):
    return render(request, "html/hours_download.html")

def dut_hours(request):
    dut = int(request.body)
    test_hours = {}
    tests = ChamberLog.objects.filter(dut_id = dut).distinct("test_id")
    for test in tests:
        total_hours = ChamberLog.objects.filter(log_id__test_id = test.log_id.test_id).filter(dut_id = dut).latest("timestamp").total_hours
        test_hours[test.log_id.test_id.test_type_id.test_name] = total_hours
    
    a = open("database/templates/html/dut_hours", "w")
    a.write("")
    a.close()
    a = open("database/templates/html/dut_hours", "a")
    a.write("{{")
    
    for i in test_hours:
        a.write( f'\"{i}\": {test_hours[i]},\n')
    a.write("}}")
    a.close()
    
    return HttpResponse("dut hours compiled")

def harness_info(request, id):
    test_list = Test_Harness.objects.filter(harness_id = id).order_by("test_id__targeted_start")
    test_history = {}
    accumulated_hours = 0
    
    if test_list.count() == 0:
        return render(request, "html/harness_info.html", {"test_history": test_history, "harness_info":Harness.objects.filter(pk = id)})
    
    for test in test_list:
        if test.date_inserted == None:
            starting_time = 0
            start_date = test.test_id.targeted_start
        else:
            start_date = test.date_inserted.date
            try:
                starting_time = ChamberLog.objects.filter(log_id__test_id = test.test_id).filter(circuit_number = test.circuit_number).filter(timestamp__gte = test.date_inserted).earliest("timestamp").total_hours
            except:
                continue
            
        if test.date_removed == None:
            try:
                ending_time = ChamberLog.objects.filter(log_id__test_id = test.test_id).filter(circuit_number = test.circuit_number).latest("timestamp").total_hours
            except:
                continue
        else:
            try:
                ending_time = ChamberLog.objects.filter(log_id__test_id = test.test_id).filter(circuit_number = test.circuit_number).filter(timestamp__lte = test.date_inserted).latest("timestamp").total_hours
            except:
                continue
            
        total_hours = ending_time - starting_time
        accumulated_hours += total_hours
        if test.test_id.test_type_id.test_name in test_history:
            test_history[test.test_id.test_type_id.test_name] = [total_hours + test_history[test.test_id.test_type_id.test_name][0], accumulated_hours, start_date, test.test_id.chamber_id.chamber_name]
        else:
            test_history[test.test_id.test_type_id.test_name] = [total_hours, accumulated_hours, start_date, test.test_id.chamber_id.chamber_name]
    
    return render(request, "html/harness_info.html", {"test_history": test_history, "harness_info":Harness.objects.filter(pk = id)})

def menu(request):
    return render(request, "html/menu.html")

class DUTListView(SingleTableMixin,  CreateView, FilterView):
    
    model = DUT
    table_class = DUTTable
    template_name = 'html/dut.html'
    filterset_class = DUTFilter
    form_class = DUTForm
    success_url = '/database/dut'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("dut"))
    def get_table_pagination(self, request):
        return False

class UpdateTableViewDUT(UpdateView):
    
    model = DUT
    template_name = 'html/update_dut.html'
    form_class = DUTForm
    success_url = '/database/dut'


def delete_item_dut(request, pk):

    DUT.objects.filter(dut_id=pk).delete()

    return HttpResponseRedirect(reverse("dut"))

class DUTInfo(SingleTableMixin, CreateView):
    template_name = 'html/dut_info.html'
    table_class = SubcomponentTable
    form_class = SubcomponentForm
    
    def get_queryset(self, *args, **kwargs):
        return Subcomponent.objects.filter(dut_id = self.kwargs.get('pk'))
    
    def get_table_pagination(self, request):
        return False
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        id = self.kwargs.get('pk')
        test_list = Test_DUT.objects.filter(dut_id = id).order_by("test_id__targeted_start")
        test_history = {}
        accumulated_hours = 0
        
        for test in test_list:
            if test.date_inserted == None:
                starting_time = 0
                start_date = test.test_id.targeted_start
            else:
                start_date = test.date_inserted.date
                try:
                    starting_time = ChamberLog.objects.filter(log_id__test_id = test.test_id).filter(circuit_number = test.circuit_number).filter(timestamp__gte = test.date_inserted).earliest("timestamp").total_hours
                except:
                    starting_time=0
                    continue
                
            if test.date_removed == None:
                try:
                    ending_time = ChamberLog.objects.filter(log_id__test_id = test.test_id).filter(circuit_number = test.circuit_number).latest("timestamp").total_hours
                except:
                    ending_time=0
                    continue
            else:
                try:
                    ending_time = ChamberLog.objects.filter(log_id__test_id = test.test_id).filter(circuit_number = test.circuit_number).filter(timestamp__lte = test.date_removed).latest("timestamp").total_hours
                except:
                    continue    
            total_hours = ending_time - starting_time
            accumulated_hours += total_hours
            if test.test_id.test_type_id.test_name in test_history:
                test_history[test.test_id.test_type_id.test_name] = [total_hours + test_history[test.test_id.test_type_id.test_name][0], accumulated_hours, start_date, test.test_id.chamber_id.chamber_name, test.circuit_number]
            else:
                test_history[test.test_id.test_type_id.test_name] = [total_hours, accumulated_hours, start_date, test.test_id.chamber_id.chamber_name, test.circuit_number]       
        context['DUT'] = {"test_history": test_history, "dut_info": DUT.objects.filter(pk = self.kwargs.get('pk'))}
        return context
    
    def get_success_url(self):
        return reverse('dut_info', kwargs={'pk': self.kwargs.get('pk')})
    

    
class UpdateTableViewSubcomponent(UpdateView):
    
    model = Subcomponent
    template_name = 'html/update_subcomponent.html'
    form_class = SubcomponentForm
    success_url = '/database/dut_info'


def delete_item_subcomponent(request, pk):
    dut_id = Subcomponent.objects.get(component_id = pk).dut_id.dut_id
    Subcomponent.objects.filter(component_id=pk).delete()
    return HttpResponseRedirect(reverse("dut_info", kwargs={'pk': dut_id}))


class DAR_ChannelListView(SingleTableMixin,  CreateView, FilterView):

    model = DARChannel
    table_class = DAR_ChannelTable
    template_name = 'html/DAR_channel.html'
    filterset_class = DAR_ChannelFilter
    form_class = DAR_ChannelForm
    success_url = '/database/dar_channel'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("DAR_Channel"))
    def get_table_pagination(self, request):
        return False

class UpdateTableView_DAR_Channel(SingleTableMixin,  UpdateView):
    
    model = DARChannel
    form_class = DAR_ChannelForm
    template_name = 'html/update.html'
    success_url = '/database/dar_channel'



def delete_DAR_Channel(request, pk):
    DARChannel.objects.filter(channel_id=pk).delete()
    return HttpResponseRedirect(reverse("DAR_Channel"))

def compileDUTList(request):
    test_id = request.body
    try:
        test_id = int(test_id)
    except:
        a = open("database/templates/html/dut_list", "w")
        a.write("")
        a.close()
        return HttpResponse("No test selected")
    else:
        program_id = Test.objects.filter(test_id=test_id)[0].program_id
        dut_list = DUT.objects.filter(product_id__program_id = program_id)
        
        a = open("database/templates/html/dut_list", "w")
        a.write("{\n")
        a.close()

        a = open("database/templates/html/dut_list", "a")
        for i in range(len(dut_list)):
            a.write(f'\"{dut_list[i].dut_id}\":\"{dut_list[i]}\"')
            if i == len(dut_list)-1:
                a.write("\n")
            else:
                a.write(",\n")
            
        a.write(f'}}')
        a.close()
        return HttpResponse("DUT list compiled")

def getDUTList(request):
    return render(request, "html/dut_list")


def compileTestPageFilterList(request):
    program_id = request.body
    try:
        program_id = int(program_id)
    except:
        a = open("database/templates/html/ProductList", "w")
        a.write("")
        a.close()
        a = open("database/templates/html/TestMapList", "w")
        a.write("")
        a.close()
        return HttpResponse("No test selected")
    else:
        product_list = Product.objects.filter(program_id = program_id)
        testmap_list = TestMap.objects.filter(program_id = program_id)
        
        a = open("database/templates/html/ProductList", "w")
        a.write("{\n")
        a.close()
        
        a = open("database/templates/html/TestMapList", "w")
        a.write("{\n")
        a.close()

        a = open("database/templates/html/ProductList", "a")
        for i in range(len(product_list)):
            a.write(f'\"{product_list[i].product_id}\":\"{product_list[i]}\"')
            if i == len(product_list)-1:
                a.write("\n")
            else:
                a.write(",\n")
            
        a.write(f'}}')
        a.close()
        
        a = open("database/templates/html/TestMapList", "a")
        for i in range(len(testmap_list)):
            a.write(f'\"{testmap_list[i].test_map_id}\":\"{testmap_list[i]}\"')
            if i == len(testmap_list)-1:
                a.write("\n")
            else:
                a.write(",\n")
            
        a.write(f'}}')
        a.close()
        
        return HttpResponse("Product and Test Map lists compiled")

def getProductList(request):
    return render(request, "html/ProductList")

def getTestMapList(request):
    return render(request, "html/TestMapList")



##################################################################################################################################################################################
# TEST PAGE

class FixturesListView(SingleTableMixin,  CreateView, FilterView):

    model = Fixtures
    table_class = FixturesTable
    template_name = 'html/fixtures.html'
    filterset_class = FixturesFilter
    form_class = FixturesForm
    success_url = '/database/Fixtures'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Fixtures"))
    def get_table_pagination(self, request):
        return False
    
class UpdateTableViewFixtures(SingleTableMixin,  UpdateView):
    
    model = Fixtures
    table_class = FixturesTable
    form_class = FixturesForm
    template_name = 'html/update.html'
    success_url = '/database/Fixtures'



def delete_fixtures(request, pk):

    Fixtures.objects.filter(Fixtures_id=pk).delete()

    return HttpResponseRedirect(reverse("Fixtures"))


# def test_view(request):
#     queryset = Test.objects.all()  # 使用模型类的 objects 属性
#     table = TestTable(queryset)  # 实例化表类
#     return render(request, 'html/test.html', {'table': table})



##################################################################################################################################################################################
