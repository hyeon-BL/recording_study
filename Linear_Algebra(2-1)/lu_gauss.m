function [ L U ] = lu_gauss(A) 
% This function computes the LU factorization of A
% Assumes A is not singular 
% And assume Gauss Elimination (GE) requires no row swaps

[n,m] = size(A);    % n = #rows, m = # columns
if n ~= m; 
    error('A is not a square matrix');
end

for k = 1:n-1      % for each row (except last)
    if A(k,k) == 0; 
        error('Null diagonal element'); 
    end
    
    for i = k+1:n            % for row i below row k
        m = A(i,k)/A(k,k);   % m = scalar for row i
        
       % Put scalar for row i in (i,k) position.  We do this to store L values. 
       %Since the lower triangular part of A gets zeroed out in GE,
       % we  use it as a storage place for values of L. 
        A(i,k) = m;  
                     
        for j = k+1:n   
            % Subtract m*row k from row i -> row i
            % We only need to do this for columns k+1 to n since the values below A(k,k) will be zero.                         
            A(i,j) = A(i,j) - m*A(k,j);
        end
    end
end
% A should be a matrix where the upper triangular part of A is the matrix U 
% and the rest of A below the diagonal is L (but missing the 1's on the diagonal). 
L = eye(n) + tril(A, -1); % eye(n) is a matrix with 1's on diagonal
U = triu(A);
end
