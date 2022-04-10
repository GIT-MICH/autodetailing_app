Final project of the 'Python Developer' course (at CodersLab)

Project idea: The purpose of the created application is to manage services in the autodetailing studio. Services can be ordered by the user who is 
logged in. After adding services to the cart, selecting the employee and the date of the meeting, you can order the service. 
When ordering, you can see a summary of what the cost will be and the approximate time to complete. 
The user can add an opinion about the service performed.

Thanks to this application, managers can efficiently organize orders, add services, modify, etc.


** APP SUMMARY ** MODELS: 0. USER

    Category, 
    Service, 
    About, 
    Cart, 
    Order, 
    Opinion

FORMS

    LoginForm
    RegisterForm
    UpdateUserPermisionForm
    AddServiceForm
    AddOpinionForm
    AddWorkerForm
    CartForm
    OrderForm

VIEWS:
    '', FirstView
    'main/', MainView
    'categories/', CategoriesView
    'outside/', OutsideServicesView
    'inside/', InsideServicesView
    'add_service/', AddServiceView
    'del_service/<int:id>/', DeleteServiceView
    'add_opinion/', AddOpinionView
    'all_opinions/', AllOpinionsView
    'add_worker/', AddWorkerView
    'services/', ServicesView
    'service/<int:id>/', ServiceDetailView
    'service_to_card/<int:service_id>/', AddServiceToCartView
    'remove_from_card/<int:service_id>/', RemoveServiceFromCartView
    'order/', CreateOrderView.as_view()
    'user_orders/', UserOrdersView
    'all_orders/', AllOrdersView
    'login/', LoginView
    'logout/', LogoutView
    'register/', RegisterView
    'all/set_permission/<int:user_id>/', UserPermissionUpdateView
    'all/', AllAccountsView

TESTS: 27
