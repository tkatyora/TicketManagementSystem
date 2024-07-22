import AdminDashboard from '@/app/componets/adminDashboard';

const DashboardPage = () => {
 
  const user = {
    first_name: 'John',
    last_name: 'Doe',
    roles: 'admin',
  };

  return (
    <div>
      <AdminDashboard user={user} />
    </div>
  );
}

export default DashboardPage;
