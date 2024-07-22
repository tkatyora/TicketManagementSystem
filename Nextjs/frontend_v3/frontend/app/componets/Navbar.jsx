import Link from 'next/link';

const Navbar = () => {
  return (
    <nav className="bg-gray-700 shadow-lg fixed top-0 w-full z-10">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex">
            <div className="flex-shrink-0">
              <Link href="/">
                <a className="text-2xl font-bold">
                  Secure<span className="text-blue-500">Ticketing</span>Solution
                </a>
              </Link>
            </div>
            <div className="hidden sm:ml-6 sm:flex sm:space-x-8">
              <Link href="/">
                <a className="text-gray-900 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium leading-5 hover:border-blue-500">
                  <i className="text-blue-500 fas fa-house"></i> Home
                </a>
              </Link>
              <Link href="/view_show">
                <a className="text-gray-900 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium leading-5 hover:border-blue-500">
                  <i className="text-blue-500 fas fa-music"></i> Performances
                </a>
              </Link>
              <Link href="#">
                <a className="text-gray-900 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium leading-5 hover:border-blue-500">
                  <i className="text-blue-500 fas fa-ticket"></i> Book a Ticket
                </a>
              </Link>
              <Link href="#">
                <a className="text-gray-900 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium leading-5 hover:border-blue-500">
                  <i className="text-blue-500 fas fa-info-circle"></i> About
                </a>
              </Link>
              <div className="relative">
                <button className="text-gray-900 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium leading-5 hover:border-blue-500">
                  <i className="text-blue-500 fas fa-user-circle"></i> Portal
                </button>
                <div className="absolute right-0 mt-2 w-48 bg-white border border-gray-200 rounded-md shadow-lg">
                  <Link href="/sign_in">
                    <a className="block px-4 py-2 text-gray-700 hover:bg-gray-100">
                      Admin Portal
                    </a>
                  </Link>
                  <Link href="#">
                    <a className="block px-4 py-2 text-gray-700 hover:bg-gray-100">
                      Customer Portal
                    </a>
                  </Link>
                </div>
              </div>
            </div>
          </div>
          <div className="flex items-center">
            <form className="flex space-x-4" role="search">
              <input
                className="form-input block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                type="search"
                placeholder="Search"
                aria-label="Search"
              />
              <button className="btn btn-primary">Search</button>
            </form>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
